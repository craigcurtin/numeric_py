import numpy as np


exp = 0
x = 2
for i in range(10):
    exp = exp + \
          ((x ** i) / np.math.factorial(i))
    print(f'Using {i}-term, {exp}')

print(f'The true e^2 is: {np.exp(2)}')