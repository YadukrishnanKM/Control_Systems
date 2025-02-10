import numpy as np
import control as ct
import matplotlib.pyplot as plt

num =   [1]         #numerator
den =   [3, 2, 8]   #dinominator

tf  =   ct.TransferFunction(num,den)    #find the transfer funnction

mag, phase, omega = ct.frequency_response(tf)   #determine the freqency responce

x, z    = np.meshgrid(omega, phase)
z, y    = np.meshgrid(mag,omega)

#2d ploting
plt.plot(omega,mag)
plt.xlabel("omega")
plt.ylabel("magnitude")
plt.title("2d omega-magnitude plot")

#3dploting
ax = plt.figure().add_subplot(projection='3d')
ax.plot_surface(x,y,z)
ax.set_xlabel("omega")
ax.set_ylabel("phase")
ax.set_title("3d omega-phase-magnitude plot")
plt.show()
