import matplotlib.pyplot as plt

bands = ["ELF/VLF", "LF", "MF", "HF", "VHF", "UHF", "SHF", "EHF",
         "Infrared", "Visible", "UV", "X-ray", "Gamma"]

start = [3e3, 3e4, 3e5, 3e6, 3e7, 3e8, 3e9, 3e10,
         3e11, 4e14, 8e14, 3e16, 3e19]

end = [3e4, 3e5, 3e6, 3e7, 3e8, 3e9, 3e10, 3e11,
       4e14, 8e14, 3e16, 3e19, 1e21]

plt.figure(figsize=(10, 4))

for i in range(len(bands)):
    plt.plot([start[i], end[i]], [i, i], marker="|")
    plt.text(start[i], i + 0.2, bands[i], fontsize=8)

plt.xscale("log")
plt.xlabel("Frequency (Hz)")
plt.title("Electromagnetic Frequency Bands")
plt.yticks([])
plt.grid()
plt.show()