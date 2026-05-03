import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_expansion_sinus(x, n_terms):
    expansion = 0
    for n in range(n_terms + 1):
        if n % 2 != 0:  # Only odd terms contribute to the sine expansion
            expansion += ((-1) ** ((n -1) // 2)) * (x ** n) / math.factorial(n)
    return expansion


x_values = np.linspace(-10, 10, 800)

y_real = np.sin(x_values)

# plotting
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_real, label='Original sin(x)', linewidth=4, color='blue', zorder=10)

# taylor approximations
terms = [1, 3, 5, 7, 9, 11, 13, 15]
colors = plt.cm.inferno(np.linspace(0.8, 0.2, len(terms)))

for i, (n, color) in enumerate(zip(terms, colors)):
    y_taylor = taylor_expansion_sinus(x_values, n)
    plt.plot(x_values, y_taylor, label=f'Taylor (Grad {n})', color=color, linewidth=2, alpha=0.8)

# Optische Anpassungen
plt.ylim(-3, 3)
plt.xlim(-10, 10)
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.grid(True, alpha=0.3)
plt.title("Taylor-Reihen Annäherung an sin(x)", fontsize=16, pad=15)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()

plt.show()
