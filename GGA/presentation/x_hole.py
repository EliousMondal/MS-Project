import numpy as np
import matplotlib.pyplot as plt

low = -3
high = 3
n_xpoints = 1000
dx = (high-low)/n_xpoints

def normalise(y,dx):
    s = np.sum(y*dx)
    return y/s

x = np.linspace(low,high,n_xpoints)
y0 = np.zeros(n_xpoints)
y1 = -normalise(np.exp(-x**2),dx)
y2 = 0.2*(2*x**2 - 1)*np.exp(-x**2)

plt.figure()
plt.title(r"Possible $\rho_x$ and $\rho_c$ for two electrons moving in 1D space")
plt.plot(x,y0,"k")
plt.plot(x,y1,label=r"$\rho_x$")
plt.plot(x,y2,label=r"$\rho_c$")
#plt.plot(x,y1+y2,label=r"$\rho_{xc}$")
plt.ylabel(r"$\rho(r,r')$ ----->")
plt.xlabel(r"$r-r'$")
plt.legend()
plt.show()
