import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2024.csv', comment='#')

transit_df = data.loc[data['discoverymethod'] == 'Transit']
radial_df = data.loc[data['discoverymethod'] == 'Radial Velocity']

log_mass_t = np.log(transit_df['pl_bmassj'])
log_mass_r = np.log(radial_df['pl_bmassj'])

log_per_t = np.log(transit_df['pl_orbper'])
log_per_r = np.log(radial_df['pl_orbper'])

fig, ax = plt.subplots(2, 2, figsize=(13, 10))

ax[0].scatter(log_per_t, log_mass_t, c='red', label='Transit')
ax[0].scatter(log_mass_r, log_per_r, c='blue', label='Radial')

ax[1].hist(log_mass_t, bins=50, range=(0, 5), label='Transit', color='red', alpha=0.5)
ax[1].hist(log_mass_r, bins=50, range=(0, 5), label='Radial', color='blue', alpha=0.5)

ax[2].hist(log_per_t, bins=50, range=(0, 5), label='Transit', color='red', alpha=0.5)
ax[2].hist(log_per_r, bins=50, range=(0, 5), label='Radial', color='blue', alpha=0.5)

plt.legend(fontsize=10)
plt.show()