import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2024.csv', comment='#')
semi_axis = data['pl_orbsmax']**2 / data['st_mass']

plt.scatter(data['pl_orbper'], semi_axis,  c='orange', alpha=0.6)
plt.xlabel('Periodo orbitale')
plt.ylabel('R_max^2 / m_st')
plt.xscale('log')
plt.yscale('log')
plt.show()