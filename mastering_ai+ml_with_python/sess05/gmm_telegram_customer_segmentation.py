# python script to demonstrate supermarket customer segmentation using dbscan


# ------------------------------------------------------------------------------------------------------
# 0. Import the required modules
# ------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

# ------------------------------------------------------------------------------------------------------
# 1. Load Data
# ------------------------------------------------------------------------------------------------------


def load_data(path: str) -> pd.DataFrame:
    """
    Load the Telco Dataset

    Parameters
    -------------
    path: str
    Path to the telco dataset CSV file

    Returns
    -------------
        DataFrame
    """

    df = pd.read_csv(path)

    # Fix TotalCharges ( common issue in teh telco customer )
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0)
    return df


# ------------------------------------------------------------------------------------------------------
# 2. Preprocessing
# ------------------------------------------------------------------------------------------------------


def preprocess(df: pd.DataFrame):
    """
    Minimal Preprocessing:
        - Select a few important features
        - Encode Churn
        - Scale Data

    Returns
    --------
        X_scaled: narray
        df_scaled: DataFrae

    """

    df = df.copy()

    # Encode target
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Select only key featreus
    features = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
    ]

    # Ensure numeric features and impute missing values before scaling
    for feature in features:
        df[feature] = pd.to_numeric(df[feature], errors="coerce")
        df[feature] = df[feature].fillna(df[feature].median())

    X = df[features].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, df


# ------------------------------------------------------------------------------------------------------
# 3. PCA Viusalization
# ------------------------------------------------------------------------------------------------------


def plot_pca(X_scaled, df):
    """
    Plot PCA projection to show overlapping clusters.


    This helps explain why GMM is useful.
    """

    pca = PCA(n_components=2)
    X_2d = pca.fit_transform(X_scaled)

    plt.figure(figsize=(7, 5))
    plt.scatter(X_2d[:, 0], X_2d[:, 1], c=df["Churn"], cmap="coolwarm", alpha=0.6)

    plt.title("PCA Projection (colored by churn)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.colorbar(label="Churn (0=no, 1=Yes)")
    plt.show()

    return X_2d


# ------------------------------------------------------------------------------------------------------
# 4. Find the optimal number of components
# ------------------------------------------------------------------------------------------------------
def find_optimal_components(X_scaled, max_k=8):

    ks = range(1, max_k + 1)
    bics = []

    for k in ks:
        gmm = GaussianMixture(n_components=k, random_state=42)
        gmm.fit(X_scaled)
        bics.append(gmm.bic(X_scaled))

    plt.figure(figsize=(6, 4))
    plt.title("Selecting Number of Clusters (BIC)")
    plt.xlabel("Number of components")
    plt.ylabel("BIC")
    plt.show()

    best_k = ks[np.argmin(bics)]
    print(f"\nOptimal number of clusters (BIC): {best_k}")

    return best_k


# ------------------------------------------------------------------------------------------------------
# 5. Train GMM Model
# ------------------------------------------------------------------------------------------------------


def train_gmm(X_scaled, n_components):
    """
    Fit the Gaussian Mixture model

    Returns:
    -------------
        labels: hard cluster assignments
        probs: soft probability
    """
    gmm = GaussianMixture(n_components=n_components, random_state=42)
    gmm.fit(X_scaled)
    labels = gmm.predict(X_scaled)
    probs = gmm.predict_proba(X_scaled)
    return gmm, labels, probs


# ------------------------------------------------------------------------------------------------------
# 6. Visualize Clusters
# ------------------------------------------------------------------------------------------------------


def plot_clusters(X_2d, labels, probs):

    confidence = probs.max(axis=1)

    plt.figure(figsize=(7, 5))

    scatter = plt.scatter(
        X_2d[:, 0],
        X_2d[:, 1],
        c=labels,
        cmap="tab10",
        alpha=0.7,
        s=confidence + 60 + 10,
    )

    plt.title("GMM Clusters (Point size = Confidence)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.colorbar(scatter)
    plt.show()


# ------------------------------------------------------------------------------------------------------
# 7. Simple Segment Interpretation
# ------------------------------------------------------------------------------------------------------


def describe_segments(df, labels):
    """Display simple business Interpretation of customer clusters."""

    df = df.copy()

    df["Segment"] = labels

    summary = df.groupby("Segment")[
        ["tenure", "MonthlyCharges", "TotalCharges", "Churn"]
    ].mean()

    print("\nSegment Summary (Mean Values)")
    print(summary.round(2))

    print("\nBusiness Interpretation")

    for seg in summary.index:
        row = seg.loc[seg]

        description = []

        if row["tenure"] < 20:
            description.append("New Customers")
        else:
            description.append("Long-term Customers")

        if row["MonthlyCharges"] > 70:
            description.append("High Spend")
        else:
            description.append("Low Spend")

        if row["Churn"] > 0.4:
            description.append("High churn risk")
        else:
            description.append("Low churn risk")

        print(f"\n Segment {seg}: " + " . ".join(description))

# ------------------------------------------------------------------------------------------------------
# 8. Main function to execut the pipeline
# ------------------------------------------------------------------------------------------------------

def main():
    print("Loading data...")
    data_file = (
        Path(__file__).resolve().parent.parent/"files"/~/Coding/Python/Edulink_Python/mastering_ai+ml_with_python/sess05/
    )

    try: 
        df = load_data(str(data_file))
    except FileNotFoundError:
        print(f"Error: File {data_file} not found")
        return
    except PermissionError:
        print(f"Error: Permission Denied when reading {data_file}")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: {data_file} is empty")
        return
    except pd.errors.ParserError:
        print(f"Error: {data_file} could not be parsed")
        return
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return

    print("Preprocessing data...")
    X_scaled, df = preprocess(df)

    print("PCA Viusalization...")
    X_2d = plot_pca(X_scaled, df)

    print("Selecting number of clusters...")
    k = find_optimal_components(X_scaled)

    print("Training GMM...")
    gmm, labels, probs = train_gmm(X_scaled, k)

    print("Viusalizing Clusters...")
    plot_clusters(X_2d, labels, probs)

    print("Interpreting segments...")
    describe_segments(df, labels)

# Run the Application

if __name__ == "__main__":
    main()


