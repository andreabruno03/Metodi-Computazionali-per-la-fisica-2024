import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data1 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M0.csv')
data2 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M1.csv')
data3 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M2.csv')
data4 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M3.csv')

fig, ax = plt.subplots(figsize=(10, 8))
plt.title('Istogramma tempi del primo modulo')
plt.hist(data1['hit_time'], bins=30)
plt.xlabel('Hit Time (ns)')
plt.ylabel('Numero di hit')
plt.show()
print(data1.columns)

delta_t = np.ma.ediff1d(data1['hit_time'])
Delta_t = np.log10(delta_t)

print(delta_t)

fig, ax = plt.subplots(figsize=(10, 8))
plt.title(r'Istogramma delle $\Delta t$ per il primo modulo')
plt.hist(Delta_t, bins=50, range=[0, 10])
plt.xlabel(r"$log_{10}(\Delta t$)")
plt.ylabel('Numero di hit')
plt.show()