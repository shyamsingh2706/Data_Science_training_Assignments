import numpy as np
import matplotlib.pyplot as plt

def yz_rotation(vector,theta):
    """Rotates 3-D vector around x-axis"""
    R = np.array([[1,0,0],
                  [0, np.cos(theta),-np.sin(theta)],
                  [0, np.sin(theta), np.cos(theta)]
                  ])
    return np.dot(R,vector)

def zx_rotation(vector,theta):
    """Rotates 3-D vector around y-axis"""
    R = np.array([[np.cos(theta),0,np.sin(theta)],
                  [0,1,0],
                  [-np.sin(theta),0,np.cos(theta)]
                  ])
    return np.dot(R,vector)

def xy_rotation(vector,theta):
    """Rotates 3-D vector around z-axis"""
    R = np.array([[np.cos(theta), -np.sin(theta),0],
                  [np.sin(theta), np.cos(theta),0],
                  [0,0,1]
                  ])
    return np.dot(R,vector)

def define_theta(theta):
    radians = np.deg2rad(theta)
    return radians


v1=np.array([4,0,4])
theta=define_theta(45)
print(" v1 : " + str(v1))

v2 = zx_rotation(v1, theta)
print(" v2 : " + str(v2))

theta=define_theta(90)
v3 = xy_rotation(v2, theta)
print(" v3 :  " + str(v3))

theta=define_theta(30)
v4 = yz_rotation(v3, theta)
print(" v4 : " + str(v4))

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(np.linspace(0,v1[0]),np.linspace(0,v1[1]),np.linspace(0,v1[2]))
ax.plot(np.linspace(0,v2[0]),np.linspace(0,v2[1]),np.linspace(0,v2[2]))
ax.plot(np.linspace(0,v3[0]),np.linspace(0,v3[1]),np.linspace(0,v3[2]))
ax.plot(np.linspace(0,v4[0]),np.linspace(0,v4[1]),np.linspace(0,v4[2]))

plt.show()