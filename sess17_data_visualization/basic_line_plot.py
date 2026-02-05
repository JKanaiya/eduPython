# Python script to demonstrate visualising student scores on a line plot

# Import the required modules
import matplotlib.pyplot as plt
import numpy as np

x_pt = np.array(["Adam", "Richard", "William", "Emy", "Linda"])
y_pt = np.array([86, 90, 79, 78, 96])
plt.plot(x_pt, y_pt,'o:r', marker='o')
plt.show()