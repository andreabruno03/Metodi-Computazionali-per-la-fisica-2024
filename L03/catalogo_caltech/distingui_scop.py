import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2024.csv', comment='#')

transit_df = data.loc[data['discoverymethod'] == 'Transit']
radial_df = data.loc[data['discoverymethod'] == 'Radial Velocity']

fig, ax = plt.subplots(figsize=(13, 8))
plt.title('Confronto massa - periodo orbitale con distinzione in base al metodo di scoperta')
plt.scatter(transit_df['pl_bmassj'], transit_df['pl_orbper'], c='red', label='Transit discoveries')
plt.scatter(radial_df['pl_bmassj'], radial_df['pl_orbper'], c='blue', label='Radial Velocity discoveries', alpha=0.5)
plt.legend(fontsize=10)
plt.xlabel('Periodo Orbitale')
plt.ylabel('Massa')
plt.xscale('log')
plt.yscale('log')
plt.show()
