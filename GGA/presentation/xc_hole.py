import numpy as np
import matplotlib.pyplot as plt

low = -5
high = 5
n_xpoints = 1000
dx = (high-low)/n_xpoints

def normalise(y,dx):
    s = np.sum(y*dx)
    return y/s

x = np.linspace(low,high,n_xpoints)
y1 = -normalise(np.exp(-x**2),dx)
y2 = -normalise(np.exp(-(x**2)/5),dx)
y3 = -normalise(np.exp(-(x**2)/10),dx)

plt.figure()
plt.title(r"Possible $\rho_{xc}$ for two electrons moving in 1D space")
plt.plot(x,y1,'r')
plt.plot(x,y2,'b')
plt.plot(x,y3,'g')
plt.ylabel(r"$\rho_{xc}(r,r')$ ----->")
plt.xlabel(r"$r-r'$")
plt.show()
