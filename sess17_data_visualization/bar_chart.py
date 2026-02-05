# Python script to demonstrate visualising student scores on a line plot

# Import the required modules
import matplotlib.pyplot as plt
import numpy as np

names = np.array(["Adam", "Richard", "William", "Emy", "Linda"])
scores = np.array([86, 90, 79, 78, 96])
plt.bar(names, scores, color="red")
plt.xlabel("Student Names")
plt.xlabel("Student Scores")
plt.title("Exam Marks")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()