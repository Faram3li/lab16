import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.log(x) + 0.7 * x**2

x = np.linspace(0.3, 12.3, 400)
y = func(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, linestyle='--', color='blue', label=r'$y = \ln x + 0.7x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції $y = \ln x + 0.7x^2$')
plt.legend()
plt.grid(True)
plt.savefig('myplot.jpg')
plt.show()
