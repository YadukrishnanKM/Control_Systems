import control as ct
import matplotlib.pyplot as plt

numrator        = [1, 2] 
denominator     = [1, 2, 3]

sys = ct.TransferFunction(numrator,denominator) #Find the Transfer function

ct.pole_zero_plot(sys)      # plot the zeros and ploes
plt.grid(True)              # turn the grid on
plt.show()