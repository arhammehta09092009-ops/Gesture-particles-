import numpy as np
import matplotlib.pyplot as plt

# Constants (set G = M = c = 1 for simplicity)
rs = 2  # Schwarzschild radius (2GM)

# Radial coordinate (must be >= rs)
r = np.linspace(rs + 0.01, 10, 500)

# Embedding function
z = 2 * np.sqrt(rs * (r - rs))

# Plot
plt.figure(figsize=(6, 6))
plt.plot(r, z, color='black')
plt.plot(r, -z, color='black')

plt.xlabel("r")
plt.ylabel("z")
plt.title("Einstein–Rosen Bridge (Embedding Diagram)")
plt.axvline(rs, linestyle='--', color='gray', label='Event Horizon')
plt.legend()

plt.grid(True)
plt.show()
