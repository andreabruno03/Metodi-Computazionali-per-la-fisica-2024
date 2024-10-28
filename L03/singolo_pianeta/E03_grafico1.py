import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv')
print(data)

print('Le colonne del data frame: ', data.columns)

#grafico flusso in funzione del tempo (linea)
plt.plot(data['TIME'], data['PDCSAP_FLUX'])
plt.xlabel('Time')
plt.ylabel('Flux')
plt.show()

#grafico flusso in funzione del tempo (punti)
plt.plot(data['TIME'], data['PDCSAP_FLUX'], 'o')
plt.title('Flusso in funzione del tempo (no linea)')
plt.xlabel('Time (Barycenter corrected Julian Date)')
plt.ylabel('Flux (electrons per second)')
plt.show()