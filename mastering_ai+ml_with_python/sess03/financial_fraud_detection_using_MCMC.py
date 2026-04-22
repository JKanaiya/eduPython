# Python script to demonstrate Financial Fraud detection using Baynesian Logistic Regression
# with Monte Carlo Markov CHain
# Features modelled:
# --  Transaction amount ( continuous + binned: low, medium, high )
# --  Location ( domestic/usual vs international/unusual )
# -- Time of day ( day/normal vs night/odd)
# -- User behaviour (normal/good vs risky/suspicious)

# We'll see the strength/influence of the above features on fraud via MCMC, then compute posterior predictive probabilities for new transaction

# TODO: Ensure that pymc & arvis modules are installed ( pip install pymc arviz)
import arviz as az
import numpy as np
import pandas as pd
import pymc as pm
from matplotlib import pyplot as plt

# ---------------------------------------------------
# 1. Synthetic Data Generation
# ---------------------------------------------------
# Data Generation Function


def generate_transaction_data(n_sample=1000, random_seed=42):
    """
    Generate synthetic transaction data with probabilistic fraud labels.

    Parameters
    -----
    n_sample: int
        Number of transactions to generate
    random_seed: int
        Seed for reproducibility

    Returns
    -----
    pandas.DataFrame
        Dataset containing features and fraud labels.
    """
    np.random.seed(random_seed)

    # continuous features
    transaction_amount = np.random.normal(loc=200, scale=120, size=n_sample)

    transaction_amount = np.clip(transaction_amount, 10, 2000)

    # Categorical features
    location = np.random.choice(
        ["domestic", "international"], size=n_sample, p=[0.75, 0.25]
    )
    time_of_day = np.random.choice(["day", "night"], size=n_sample, p=[0.65, 0.35])
    user_behaviour = np.random.choice(
        ["normal", "risky"], size=n_sample, p=[0.82, 0.18]
    )

    # binned amount for intuitive interpretation
    amount_bin = pd.cut(
        transaction_amount, [0, 100, 500, np.inf], labels=["low", "medium", "high"]
    )

    # fraud generation: influenced by all above features ( stronger effect from risky behaviour & international transactions )
    fraud_prob = (
        0.15 * (transaction_amount > 400)
        + 0.35 * (location == "international")
        + 0.25 * (time_of_day == "night")
        + 0.55 * (user_behaviour == "risky")
        + np.random.normal(0, 0.05, n_sample)  # introduce some noise
    )

    # calculate fraud
    fraud = np.random.binomial(1, np.clip(fraud_prob, 0.02, 0.95))

    data = pd.DataFrame(
        {
            "transaction_amount": transaction_amount,
            "amount_bin": amount_bin,
            "location": location,
            "time_of_day": time_of_day,
            "user_behaviour": user_behaviour,
            "fraud": fraud,
        }
    )

    # display the generated data
    print(f"Generated {n_sample} trasactions. Fraud rate: {fraud.mean():.3%}")
    return data


# ---------------------------------------------------
# 2. Buld the Baynesian Logistic Regression Model
# ---------------------------------------------------
# Baynesian Logistic Regression Model Function


def build_fraud_model(data):
    # TODO: write function doc string
    # Encode the Categorical data to numeric
    location_int = (data["location"] == "international").astype(int)
    time_int = (data["time_of_day"] == "night").astype(int)
    behaviour_int = (data["user_behaviour"] == "risky").astype(int)

    # scale continuous feature for better sampling
    amount_scaled = data["transaction_amount"] / 100.0

    with pm.Model() as model:
        # Weekly informative priors
        intercept = pm.Normal("intercept", mu=0, sigma=2)
        beta_amount = pm.Normal("beta_amount", mu=0, sigma=1)
        beta_location = pm.Normal("beta_location", mu=0, sigma=1.5)
        beta_time = pm.Normal("beta_time", mu=0, sigma=1)
        beta_behaviour = pm.Normal("beta_behaviour", mu=0, sigma=2)

        # Linear predictor
        logit_p = (
            intercept
            + beta_amount * amount_scaled
            + beta_location * location_int
            + beta_time * time_int
            + beta_behaviour * behaviour_int
        )

        # likelihood
        p_fraud = pm.Deterministic("p_fraud", pm.math.sigmoid(logit_p))
        observed = pm.Bernoulli("observed_fraud", p=p_fraud, observed=data["fraud"])

    return model


# ---------------------------------------------------
# 3. Run remote Monte Carlo Markov Chain (MCMC) Sampling
# ---------------------------------------------------


def run_mcmc(model, draws=200, tune=100, target_accept=0.95):
    # TODO: write function doc string
    with model:
        trace = pm.sample(
            draws=draws,
            tune=tune,
            chains=4,
            target_accept=target_accept,
            return_inferencedata=True,
            progressbar=True,
        )
    return trace


# ---------------------------------------------------
# 4. Analyse and make predictions
# ---------------------------------------------------
def analyse_results(trace, data):
    """
    Analyse posterior results and compute prediction for a new transaction.

    Parameters
    ----------
    trace : arviz.InferenceData
        Posterior samples.
    data : pandas.DataFrame
        Original dataset.
    """
    print("\n=== Posterior Summary (Coefficients) ===")
    summary = az.summary(
        trace,
        var_names=[
            "intercept",
            "beta_amount",
            "beta_location",
            "beta_time",
            "beta_behaviour",
        ],
    )
    print(summary)
    az.plot_trace(
        trace,
        var_names=[
            "intercept",
            "beta_amount",
            "beta_location",
            "beta_time",
            "beta_behaviour",
        ],
    )
    plt.tight_layout()
    plt.show()

    new_transaction = {
        "amount": 650,
        "location": "international",
        "time_of_day": "night",
        "user_behaviour": "risky",
    }

    # post = trace.posterior
    # amount_scaled = new_transaction["amount"] / 100.0
    # loc_int = 1 if new_transaction["location"] == "international" else 0
    # time_int = 1 if new_transaction["time_of_day"] == "night" else 0
    # beh_int = 1 if new_transaction["user_behaviour"] == "risky" else 0
    #
    # logit_samples = (
    #     post["intercept"]
    #     + post["beta_location"] * amount_scaled
    #     + post["amount"] * loc_int
    #     + post["beta_time"] * time_int
    #     + post["beta_behaviour"] * beh_int
    # )
    #
    # p_fraud_samples = 1 / (1 + np.exp(-logit_samples))
    # mean_prob = p_fraud_samples.mean().item()
    # hdi = az.hdi(p_fraud_samples, hdi_prob=0.94)
    #
    amount_scaled = new_transaction["amount"] / 100.0
    loc_int = int(new_transaction["location"] == "international")
    time_int = int(new_transaction["time_of_day"] == "night")
    beh_int = int(new_transaction["user_behaviour"] == "risky")

    # extract the posterior samples as flattened arrays
    post = trace.posterior

    # stack the chains and draws to get 1d arrays of samples
    intercept_samples = post["intercept"].stack(sample=("chain", "draw")).values
    beta_amount_samples = post["beta_amount"].stack(sample=("chain", "draw")).values
    beta_location_samples = post["beta_location"].stack(sample=("chain", "draw")).values
    beta_behaviour_samples = (
        post["beta_behaviour"].stack(sample=("chain", "draw")).values
    )
    beta_time_samples = post["beta_time"].stack(sample=("chain", "draw")).values

    # Compute the logit samples
    logit_samples = (
        intercept_samples
        + beta_amount_samples * amount_scaled
        + beta_location_samples * loc_int
        + beta_time_samples * time_int
        + beta_behaviour_samples * beh_int
    )

    # convert to probability
    p_samples = 1 / (1 + np.exp(-logit_samples))  # probability of overflow

    # mean probability
    mean_prob = float(p_samples.mean())

    # HDI
    hdi = az.hdi(p_samples, hdi_prob=0.94)
    lower = hdi[0]
    upper = hdi[1]

    print("\n=== New Transaction Risk Assessment ===")
    print(f"Transaction: {new_transaction}")
    print(f"Estimated P(Fraud) = {mean_prob:.4f}94% HDI: [{hdi[0]:.4f}, {hdi[1]:.4f}]")

    if mean_prob > 0.75:
        print("HIGH RISK - Strong Indication of Fraud")
    elif mean_prob > 0.4:
        print("Medium Risk = Recommend Manual Review")
    else:
        print("Low Risk - Likely Legitimate")


# ---------------------------------------------------
#  Run the Application
# ---------------------------------------------------

if __name__ == "__main__":
    print("Financial Fraud Detection - Baynesian Network Using MCMC")

    # a) Generate Data
    data = generate_transaction_data(n_sample=1200)

    # b) Build the model
    model = build_fraud_model(data)

    # c) Run MCMC
    trace = run_mcmc(model, draws=1500, tune=800)

    # d) Analyse and predict an example transaction
    analyse_results(trace, data)
