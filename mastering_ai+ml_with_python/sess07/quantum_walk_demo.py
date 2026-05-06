import matplotlib.pyplot as plt
import numpy as np

# Define parameters
num_steps = 100
num_nodes = 11
initial_position = num_nodes // 2

# define shift operators for the quantum walk
shift_left = np.roll(np.eye(num_nodes), -1, axis=0)
shift_right = np.roll(np.eye(num_nodes), 1, axis=0)

# Initialize probability aptitude for each node
prob_amplitudes = np.zeros(num_steps, dtype=np.complex128)
prob_amplitudes[initial_position] = 1.0

# Define the shift operators for the quantum walk
for step in range(num_steps):
    # Apply shift operators to update the probability distribution
    prob_amplitudes = 0.5 * (
        np.dot(shift_left, prob_amplitudes) + np.dot(shift_right, prob_amplitudes)
    )

# Plot the probability distribution
plt.figure(figsize=(12, 8))
plt.bar(np.arange(num_nodes), np.abs(prob_amplitudes) ** 2, color="skyblue", alpha=0.7)
plt.title("Quantum walk on a line graph")
plt.xlabel("Node")
plt.ylabel("Probability")
plt.xticks(np.arange((num_nodes)))
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()
