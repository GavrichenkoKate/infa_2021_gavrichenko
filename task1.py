import numpy as np
a = 1
b = 10
c = 1000
x = a
print(np.log(np.e**(1/(1+np.sin(x)))/(5/4+1/x**15))/np.log(1+x**2))
x = b
print(np.log(np.e**(1/(1+np.sin(x)))/(5/4+1/x**15))/np.log(1+x**2))
x = c
print(np.log(np.e**(1/(1+np.sin(x)))/(5/4+1/x**15))/np.log(1+x**2))
