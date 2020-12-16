import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,1000)
y =10*(1-np.exp(-(x-1)))**2
ypts = [2,4,6]

def x_pts(ypt):
    a = 1-np.log(1-np.sqrt(ypt/10))
    b = 1-np.log(1+np.sqrt(ypt/10))
    return a,b

z1 = [2 for i in range(10)]
z2 = [3 for i in range(10)]
z3 = [3.8 for i in range(10)]
z4 = [4.5 for i in range(10)]

x1 = np.linspace(x_pts(2)[0],x_pts(2)[1],10)
x2 = np.linspace(x_pts(3)[0],x_pts(3)[1],10)
x3 = np.linspace(x_pts(3.8)[0],x_pts(3.8)[1],10)
x4 = np.linspace(x_pts(4.5)[0],x_pts(4.5)[1],10)

y2 =15*(1-np.exp(-(x-1.5)))**2-2

def x_pts2(ypt):
    a = 1.5-np.log(1-np.sqrt((ypt+2)/15))
    b = 1.5-np.log(1+np.sqrt((ypt+2)/15))
    return a,b

z5 = [0 for i in range(10)]
z6 = [1 for i in range(10)]
z7 = [1.8 for i in range(10)]
z8 = [2.5 for i in range(10)]

x5 = np.linspace(x_pts2(0)[0],x_pts2(0)[1],10)
x6 = np.linspace(x_pts2(1)[0],x_pts2(1)[1],10)
x7 = np.linspace(x_pts2(1.8)[0],x_pts2(1.8)[1],10)
x8 = np.linspace(x_pts2(2.5)[0],x_pts2(2.5)[1],10)


plt.plot(x,y,"g")
plt.plot(x1,z1,"g")
plt.plot(x2,z2,"g")
plt.plot(x3,z3,"g")
plt.plot(x4,z4,"g")
plt.plot(x,y2,"r")
plt.plot(x5,z5,"r")
plt.plot(x6,z6,"r")
plt.plot(x7,z7,"r")
plt.plot(x8,z8,"r")
plt.show()
