import numpy as np
import matplotlib.pyplot as plt

R = 6370


h = np.geomspace(1e-3, 4e+5, 1000)  

f = R * np.arccos(R / (R + h))

plt.figure(figsize=(20, 10))
plt.semilogx(h, f, label=r"$f(h) = R \arccos\left(\frac{R}{R+h}\right)$")

plt.xlabel("h")
plt.ylabel("f(h)")
plt.title("Plot for h ∈ [1e-3, 4e+5]")
plt.grid(True)
plt.legend()
plt.show()

