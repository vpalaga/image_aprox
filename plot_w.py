import matplotlib.pyplot as plt
import numpy as np
import os, json


# Path where exe (or script) lives
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "moves.json")

with open(file_path, "r") as f:
    data = json.load(f)



N = 21
y = [d[-1] for k, d in data.items()]
x = np.linspace(0, len(y), len(y))


# fit a linear curve and estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')
ax.set_title("with of lines")
plt.show()