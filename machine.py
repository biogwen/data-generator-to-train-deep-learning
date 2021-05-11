import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x = np.linspace(0, 10, 10)
y= x**2
plt.scatter(x, y)

f = interp1d(x, y, kind='linear')
new_x = np.linspace(0, 10, 30)
result = f(new_x)

plt.scatter(x, y)
plt.scatter(new_x, result, c='r')
optimize