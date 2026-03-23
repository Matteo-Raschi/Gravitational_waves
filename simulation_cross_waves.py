import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  

A_cross = 0.2 
t = np.linspace(0, 2, 100)
frequency = 1 #Hz
omega = 2*np.pi*frequency
h_cross_t = A_cross * np.cos(omega*t) 

#define the distribution of points along the circunference of radius 1 on the yz plane


theta = np.linspace(0, 2*np.pi, 100)
y = np.cos(theta)
z = np.sin(theta)

#now i need to define the deformation of our points 

new_y = []
new_z = []

for i in range(len(t)):
    new_y.append(y - 1/2*h_cross_t[i] * z)
    new_z.append(z - 1/2*h_cross_t[i] * y)


fig, ax = plt.subplots()
line, = ax.plot(new_y[0], new_z[0])
ax.set_aspect("equal")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

def update(i):
    line.set_data(new_y[i], new_z[i])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), interval=20)

plt.show()





