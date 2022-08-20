from scipy.optimize import fsolve


# Compute the root of the function 𝑓(𝑥)=𝑥3−100𝑥2−𝑥+100

f = lambda x: x**3-100*x**2-x+100

print( fsolve(f, [2, 80]) )
