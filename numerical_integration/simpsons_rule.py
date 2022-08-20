import numpy as np
# Simpson’s Rule to approximate ∫𝜋0sin(𝑥)𝑑𝑥 with 11 evenly spaced grid points over the whole interval.
a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) \
            + 4*sum(f[1:n-1:2]) + f[n-1])
err_simp = 2 - I_simp

print(I_simp)
print(err_simp)