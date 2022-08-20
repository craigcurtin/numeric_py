import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')


labels = ['First Order', 'Third Order', 'Fifth Order', 'Seventh Order']

x = np.pi / 2
y = 0

for n in range(4):
    y = y + ((-1) ** n * (x) ** (2 * n + 1)) / np.math.factorial(2 * n + 1)

print(y)
x = np.linspace(0, 3, 30)
y = np.exp(x)

plt.figure(figsize = (14, 4.5))
plt.subplot(1, 3, 1)
plt.plot(x, y)
plt.grid()
plt.subplot(1, 3, 2)
plt.plot(x, y)
plt.grid()
plt.xlim(1.7, 2.3)
plt.ylim(5, 10)
plt.subplot(1, 3, 3)
plt.plot(x, y)
plt.grid()
plt.xlim(1.92, 2.08)
plt.ylim(6.6, 8.2)
plt.tight_layout()
plt.show()