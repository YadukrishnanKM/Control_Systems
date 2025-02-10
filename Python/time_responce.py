import numpy as np
import control as ct
import matplotlib.pyplot as plt

num = [1]
den = [1, 2, 3]

A = [[-2, -3],
     [ 1,  0]]

B = [[1],
     [0]]

C = [[0, 1,]]

D = [[0]]

sys = ct.ss(A, B, C, D)
print(sys)


#step reponse
timeVector          =   np.linspace(0,5,500)
time_return,sys_out =   ct.step_response(sys,timeVector)

plt.subplot(1,2,1)
plt.plot(time_return,sys_out)
plt.title("step response")
plt.xlabel("time")
plt.ylabel("sys output magnitude")

#impulse reponse
timeVector          =   np.linspace(0,5,500)
time_return,sys_out =   ct.impulse_response(sys,timeVector)

plt.subplot(1,2,2)
plt.plot(time_return,sys_out)
plt.title("impulse response")
plt.xlabel("time")
plt.ylabel("sys output magnitude")

plt.show()