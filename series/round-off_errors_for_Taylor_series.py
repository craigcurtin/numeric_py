
import numpy as np

exp = 0
x = -30
for i in range(200):
    exp = exp + \
          ((x ** i) / np.math.factorial(i))

print(f'Using {i}-term, our result is {exp}')
print(f'The true e^2 is: {np.exp(x)}')