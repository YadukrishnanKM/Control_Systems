import control as ctrl

# Define transfer functions for system components
G1 = ctrl.TransferFunction([1], [1, 2])  # G1(s) = 1 / (s + 2)
G2 = ctrl.TransferFunction([1, 3], [1, 4])  # G2(s) = (s + 3) / (s + 4)
H1 = ctrl.TransferFunction([1], [1, 5])  # H1(s) = 1 / (s + 5)

# Series connection: G1 * G2
G_series = ctrl.series(G1, G2)

# Feedback connection: G_series / (1 + G_series * H1)
G_closed_loop = ctrl.feedback(G_series, H1)

# Display the final transfer function
print("Equivalent Transfer Function:")
print(G_closed_loop)
