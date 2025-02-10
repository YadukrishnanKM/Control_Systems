import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function
# Example: G(s) = 5 / (s^2 + 2s + 3)
num = [5]
den = [1, 2, 3] 

G = ctrl.TransferFunction(num, den)

ctrl.nyquist(G, omega=np.logspace(-2, 2, 1000))  # Logarithmic frequency range

plt.grid(True)

plt.show()
