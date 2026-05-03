# python script to demonstrate Federated learning for keyboard next-word prediction

# the script simulates Federated learning across multiple users ( Rand, Mat, Ganoes) using synthetic data
# It includes training metrics and visualisation

# ------------------------------------------------------------------------------------------------------
# 0. Import the required modules
# ------------------------------------------------------------------------------------------------------
import copy
import random
from typing import Dict, List

import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# ------------------------------------------------------------------------------------------------------
# 1. Generate a synthetic Dataset
# ------------------------------------------------------------------------------------------------------


def generate_sentences(base_phrase, variations=80):

    sentences = []
    fillers = ["please", "today", "now", "later", "quickly", "kindly"]
    endings = ["", "please", "now", "thanks", "ok", "kindly"]

    for _ in range(variations):
        phrase = random.choice(base_phrase)
        words = phrase.split()

        if random.random() > 0.5:
            pos = random.randint(0, len(words) - 1)
            words.insert(pos, random.choice(fillers))

        words.append(random.choice(endings))
        sentences.append(" ".join(words).strip())
    return sentences


# Base phrases for each user(device)
rand_base = [
    "hello, how are you",
    "how is your day",
    "are you coming today",
    "Let us meet later",
    "please call me",
]

mat_base = [
    "hi how are things",
    "are you doing well",
    "what are you doing",
    "Let us catch up",
    "text me later",
]

ganoes_base = [
    "hello, are you ok",
    "how have you been",
    "life is interesting",
    "the deck is restless",
    "im good",
]

patrick_base = [
    "hello",
    "the inner machinations of my mind are an enigma",
    "the rock is a rock",
    "NO",
    "what?",
]

# Generate the dataset
data: Dict[str, list[str]] = {
    "rand": generate_sentences(rand_base),
    "mat": generate_sentences(mat_base),
    "ganoes": generate_sentences(ganoes_base),
    "patrick": generate_sentences(patrick_base),
}

# ------------------------------------------------------------------------------------------------------
# 2. Vocabulary
# ------------------------------------------------------------------------------------------------------


def build_vocab(sentences: List[str]) -> Dict[str, int]:
    words = []
    for s in sentences:
        words.extend(s.split())

    vocab = {
        w: n + 1 for n, w in enumerate(set(words))
    }  # use set to filter ducplicates
    vocab["<PAD>"] = 0
    return vocab


all_sentences = sum(data.values(), [])
vocab = build_vocab(all_sentences)
vocab_size = len(vocab)

# ------------------------------------------------------------------------------------------------------
# 3. Dataset
# ------------------------------------------------------------------------------------------------------


class TextDataset(Dataset):
    def __init__(self, sentences, vocab, seq_len=3):
        self.data = []

        for sentence in sentences:
            tokens = [vocab[w] for w in sentence.split()]
            for n in range(len(tokens) - seq_len):
                self.data.append((tokens[n : n + seq_len], tokens[n + seq_len]))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x, y = self.data[idx]
        return torch.tensor(x), torch.tensor(y)


# ------------------------------------------------------------------------------------------------------
# 4. The model
# ------------------------------------------------------------------------------------------------------


class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embed_size=16, hidden_size=32):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])


# ------------------------------------------------------------------------------------------------------
# 5. Training and Evaluation
# ------------------------------------------------------------------------------------------------------
def train(model, loader, epoch=1):
    criterion = nn.CrossEntropyLoss()
    optimiser = optim.Adam(model.parameters(), lr=0.01)

    model.train()
    for _ in range(epoch):
        for x, y in loader:
            optimiser.zero_grad()
            preds = model(x)
            loss = criterion(preds, y)
            loss.backward()
            optimiser.step()


def evaluate_loss(model, loader):
    criterion = nn.CrossEntropyLoss()
    model.eval()
    loss = 0

    with torch.no_grad():
        for x, y in loader:
            loss += criterion(model(x), y).item()
    return loss / len(loader)


def evaluate_accuracy(model, loader):
    model.eval()
    correct, total = 0, 0

    with torch.no_grad():
        for x, y in loader:
            preds = model(x)
            predicted = torch.argmax(preds, dim=1)
            correct += (predicted == y).sum().item()
            total += y.size(0)

    return correct / total


# ------------------------------------------------------------------------------------------------------
# 6. Federated Averaging
# ------------------------------------------------------------------------------------------------------
def federated_average(models):

    global_model = copy.deepcopy(models[0])
    global_dict = global_model.state_dict()

    for key in global_dict:
        global_dict[key] = torch.stack(
            [m.state_dict()[key].float() for m in models]
        ).mean(0)

    global_model.load_state_dict(global_dict)
    return global_model


# ------------------------------------------------------------------------------------------------------
# 7. DataLoaders
# ------------------------------------------------------------------------------------------------------
client_loaders = {
    name: DataLoader(TextDataset(sentences, vocab), batch_size=4, shuffle=True)
    for name, sentences in data.items()
}

# ------------------------------------------------------------------------------------------------------
# 8. Federated Training
# ------------------------------------------------------------------------------------------------------


def federated_training(rounds=5):
    global_model = LSTMModel(vocab_size)

    losses, accuracies = [], []

    for r in range(rounds):
        print(f"\n======= Round {r + 1} =======")

        local_models = []
        local_losses = []
        local_accuracies = []

        for name, loader in client_loaders.items():
            print(f"Training on {name}'s device ...")

            local_model = copy.deepcopy(global_model)
            train(local_model, loader)

            loss = evaluate_loss(local_model, loader)
            accuracy = evaluate_accuracy(local_model, loader)

            local_losses.append(loss)
            local_accuracies.append(accuracy)
            local_models.append(local_model)

        global_model = federated_average(local_models)

        avg_loss = sum(local_losses) / len(local_losses)
        avg_accuracy = sum(local_accuracies) / len(local_accuracies)

        losses.append(avg_loss)
        accuracies.append(avg_accuracy)

        print(f"Loss: {avg_loss: .3f}, Accuracy: {avg_accuracy:.3f}")

    return global_model, losses, accuracies


# ------------------------------------------------------------------------------------------------------
# 9. Prediciton
# ------------------------------------------------------------------------------------------------------


def predict_next_words(model, text, top_k=3):
    model.eval()
    tokens = text.split()[-3:]
    indices = [vocab.get(w, 0) for w in tokens]

    x = torch.tensor(indices).unsqueeze(0)

    with torch.no_grad():
        probs = torch.softmax(model(x), dim=1)

    top_indices = torch.topk(probs, top_k).indices.squeeze().tolist()
    inv_vocab = {i: w for w, i in vocab.items()}

    return [inv_vocab[i] for i in top_indices]


# ------------------------------------------------------------------------------------------------------
# 10. Plot Metrics
# ------------------------------------------------------------------------------------------------------


def plot_metrics(losses, accuracies):
    rounds = range(1, len(losses) + 1)

    plt.figure()
    plt.plot(rounds, losses)
    plt.xlabel("Rounds")
    plt.ylabel("Loss")
    plt.title("Loss over Rounds")
    plt.show()

    plt.figure()
    plt.plot(rounds, accuracies)
    plt.xlabel("Rounds")
    plt.ylabel("Accuracy")
    plt.title("Accuracy over Rounds")
    plt.show()


# ------------------------------------------------------------------------------------------------------
# 11. Run the Script
# ------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    global_model, losses, accuracies = federated_training(rounds=5)

    plot_metrics(losses, accuracies)

    print("\nPredictions")
    print("how are you -> ", predict_next_words(global_model, "how are you"))
    print("hello, how are -> ", predict_next_words(global_model, "hello, how are"))
