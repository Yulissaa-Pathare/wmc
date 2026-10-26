import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(0, 5, 1000)
rssi = 5 * np.sin(10 * d) + 3 * np.sin(22 * d)

plt.plot(d, rssi)
plt.axhline(5, color='red', linestyle='--')
plt.xlabel("Distance (m)")
plt.ylabel("Signal level (dB)")
plt.title("Multipath Fading")
plt.grid()
plt.show()