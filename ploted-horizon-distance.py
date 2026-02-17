import numpy as np
import matplotlib.pyplot as plt

R = 1.0


h = np.linspace(0, 10000, 10000)  

f = R * np.arccos(R / (R + h))

plt.figure(figsize=(20, 10))
plt.loglog(h, f, label=r"$f(h) = R \arccos\left(\frac{R}{R+h}\right)$")

plt.xlabel("h")
plt.ylabel("f(h)")
plt.title("Plot for h ∈ [0, +10000]")
plt.grid(True)
plt.legend()
plt.show()

