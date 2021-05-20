import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def split(x, y, f_upper, a, b, const=0):
    z = y - a * x - b
    f_lower = f_upper.copy()
    f_upper[z < 0] = const
    f_lower[z > 0] = const
    return f_upper, f_lower

def solve_eq(func, args, bounds=None, method=None, ig=0):
    solutions = np.array([])
    for arg in args:
        res = minimize(func, ig, args=arg, method=method, bounds=bounds)
        if not res.success:
            print('Error:', res.message)
            break
        solutions = np.append(solutions, res.x)

    return solutions

