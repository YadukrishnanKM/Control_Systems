from scipy import signal
import matplotlib.pyplot as plt

num = [1]
den = [1, 2, 3]

sys = signal.TransferFunction(num, den)
w, mag, phase = signal.bode(sys)

plt.subplot(2,1,1)
plt.semilogx(w, mag)    # Bode magnitude plot
plt.title("Magnitude")
plt.ylabel("Angle")
plt.grid(True)

plt.subplot(2,1,2)
plt.semilogx(w, phase)  # Bode phase plot
plt.title("Phase")
plt.ylabel("Angle")
plt.grid(True)

plt.show()