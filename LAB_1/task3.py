import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.log(x**2+1)/np.log(1+np.tan(1/(1+np.sin(x)**2)))*np.e**(-abs(x)/10))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()