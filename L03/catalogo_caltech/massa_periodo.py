import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2024.csv', comment='#')
print(data.columns)
print(data.head)

plt.scatter(data['pl_bmassj'], data['pl_orbper'])
plt.title('Confronto massa - periodo orbitale')
plt.xlabel('Massa')
plt.ylabel('Periodo')
plt.xscale('log')
plt.yscale('log')
plt.show()

plt.show()