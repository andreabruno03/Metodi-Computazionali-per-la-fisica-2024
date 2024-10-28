import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2024.csv', comment='#')

transit_df = data.loc[data['discoverymethod'] == 'Transit']
radial_df = data.loc[data['discoverymethod'] == 'Radial Velocity']

log_mass_t = np.log(transit_df['pl_bmassj'])
log_mass_r = np.log(radial_df['pl_bmassj'])

fig, ax = plt.subplots(figsize=(13, 10))
n1, bins1, p1 = plt.hist(log_mass_t, bins=50, range=(0, 5), label='Transit', color='red', alpha=0.5)
n2, bins2, p2 = plt.hist(log_mass_r, bins=50, range=(0, 5), label='Radial', color='blue', alpha=0.6)
plt.title('Istogramma masse')
plt.xlabel('Massa (jupiter mass)')
plt.legend(fontsize=10)
plt.show()