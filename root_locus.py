import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function

numerator = [1,2,6]
denominator = [1, 8, 2, 5]

# Create the transfer function
system = ctrl.TransferFunction(numerator, denominator)

# Plot the root locus
ctrl.root_locus(system)

# Show the plot
plt.title('Root Locus Plot')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.grid(True)
plt.show()
