pkg load control
clear all
close all
clc

G1 = tf([1], [1 2])  # G1(s) = 1 / (s + 2)
G1 = tf([1], [1 2])  # G1(s) = 1 / (s + 2)
G2 = tf([1 3], [1 4])  # G2(s) = (s + 3) / (s + 4)
H1 = tf([1], [1 5])  # H1(s) = 1 / (s + 5)

# Series connection: G1 * G2
G_series = series(G1, G2)

# Feedback connection: G_series / (1 + G_series * H1)
G_closed_loop = feedback(G_series, H1)

# Display the final transfer function
display("Equivalent Transfer Function:")
display(G_closed_loop)