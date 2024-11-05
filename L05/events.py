import reco
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M0.csv')
data2 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M1.csv')
data3 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M2.csv')
data4 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M3.csv')

def data1_to_hit():
    arr = np.empty(0)
    for i, d in data1.iterrows():
       arr = np.append(arr, reco.hit(id_m=d['mod_id'], id_s=d['det_id'], time_stamp=d['hit_time']))
    return arr


def data2_to_hit():
    arr = np.empty(0)
    for i, d in data2.iterrows():
       arr = np.append(arr, reco.hit(id_m=d['mod_id'], id_s=d['det_id'], time_stamp=d['hit_time']))
    return arr

def data3_to_hit():
    arr = np.empty(0)
    for i, d in data3.iterrows():
       arr = np.append(arr, reco.hit(id_m=d['mod_id'], id_s=d['det_id'], time_stamp=d['hit_time']))
    return arr

def data4_to_hit():
    arr = np.empty(0)
    for i, d in data4.iterrows():
       arr = np.append(arr, reco.hit(id_m=d['mod_id'], id_s=d['det_id'], time_stamp=d['hit_time']))
    return arr

res1 = data1_to_hit()
res2 = data2_to_hit()
res3 = data3_to_hit()
res4 = data4_to_hit()


res1 = list(res1)
res2 = list(res2)
res3 = list(res3)
res4 = list(res4)

all_hit = res1 + res2 + res3 + res4
print(res1[1] > res2[1])
all_hit = np.array(all_hit)
all_hit_sorted = sorted(all_hit, key=lambda x: x.time_stamp, reverse=False)


time = np.empty(0)
for i in all_hit_sorted:
    time = np.append(time, i.time_stamp)

delta_time = np.log10(time)

fig, ax = plt.subplots(figsize=(10, 8))
plt.title(r'Istogramma delle $\Delta t$ per il primo modulo')
plt.hist(delta_time, bins=50, range=[0, 10])
plt.xlabel(r"$log_{10}(\Delta t$)")
plt.ylabel('Numero di hit')
plt.show()
