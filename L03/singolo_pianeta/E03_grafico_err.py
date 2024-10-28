import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv')



plt.errorbar(data['TIME'], data['PDCSAP_FLUX'], yerr=data['PDCSAP_FLUX_ERR'], fmt='.', ecolor='red')
plt.title('Flusso in funzione del tempo (con errore)')
plt.xlabel('Time (Barycenter corrected Julian Date)')
plt.ylabel('Flux (electrons per second)')

plt.savefig('Grafico_con_errore.png')
plt.show()

