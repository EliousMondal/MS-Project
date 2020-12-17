import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,1000)

def V11(x):
    A = 0.01
    B = 1.6
    if x > 0:
        return A*(1-np.exp(-B*x))
    else:
        return -A*(1-np.exp(B*x))

def V12(x):
    C = 0.005
    D = 1.0
    return C*np.exp(-D*x**2)

y11 = np.array([V11(i) for i in x])
y22 = -y11
y12 = np.array([V12(i) for i in x])

out_file = open("outfile.txt","w")
for i in range(len(x)):
    out_file.write("{:14.8f}    {:14.8f}    {:14.8f}    {:14.8f}\n".format(x[i],y11[i],y22[i],y12[i]))
out_file.close()

plt.plot(x,y11,label=r"$V_{11}$")
plt.plot(x,y22,label=r"$V_{22}$")
plt.plot(x,5*y12,label=r"$V_{12}$")
plt.xlabel(r"x (au)")
plt.ylabel("Energy (au) ----->")
plt.legend()
plt.show()
