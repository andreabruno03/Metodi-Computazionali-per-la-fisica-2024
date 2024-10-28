import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv')

new_data = data.loc[(data['TIME'] < 939.7) & (data['TIME'] > 939)]
new_time = new_data['TIME']
new_flux = new_data['PDCSAP_FLUX']
new_err = new_data['PDCSAP_FLUX_ERR']

plt.errorbar(new_time, new_flux, yerr=new_err, fmt='.')
plt.title('Flusso in funzione del tempo (con errore), intorno a minimo')
plt.xlabel('Time (Barycenter corrected Julian Date)')
plt.ylabel('Flux (electrons per second)')

plt.show()