import numpy as np
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]

p, v = np.polyfit(x, y, deg=2, cov=True)
print(p)
print(v)

f = np.poly1d(p)

x_ = np.arange(1, 5.01, 0.005)

a = str(float('{:.3f}'.format(p[0])))
b = str(float('{:.3f}'.format(p[1])))
c = str(float('{:.3f}'.format(p[2])))


s = r'$f(x)=$' + a + r'$x^2$' + b + r'$x$' + r'$+$' +  c
plt.plot(x_, f(x_))
plt.title(s)


plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')

plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()
plt.legend()
plt.savefig('poly_deg2.png')
plt.show()


