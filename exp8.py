import numpy as np
import matplotlib.pyplot as plt

snr = [0, 2, 4, 6, 8, 10]

ber_noise = [0.08, 0.04, 0.012, 0.002, 0.0002, 0.00001]
ber_sir6 = [0.15, 0.12, 0.09, 0.07, 0.06, 0.05]
ber_sir3 = [0.25, 0.22, 0.19, 0.17, 0.15, 0.13]

plt.figure(figsize=(8, 4))
plt.semilogy(snr, ber_noise, marker='o', label="Only Noise")
plt.semilogy(snr, ber_sir6, marker='s', label="SIR 6 dB")
plt.semilogy(snr, ber_sir3, marker='d', label="SIR 3 dB")

plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("Effect of Noise and Interference on BER (BPSK)")
plt.grid()
plt.legend()
plt.show()