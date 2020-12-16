import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,1000)
y = np.exp(-0.25*x**2)

plt.plot(x,y,"r")
plt.fill_between(x,y,color="red")
plt.show()
