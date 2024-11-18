import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy import optimize

data = pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')
print(data.head)

mass = np.sqrt(np.power(data['E1'] + data['E2'], 2) - ( np.power(data['px1'] + data['px2'], 2) + np.power(data['py1'] + data['py2'], 2) + 
                                                       np.power(data['pz1'] + data['pz2'], 2) ))

# istogramma
plt.hist(mass, bins=50, range=[3.62, 3.7])
plt.title('Distribuzione massa invariante')
plt.xlabel('Massa invariante (GeV)')
plt.show()







n1, bins1, patches1 = plt.hist(mass, bins=100, range=[2.80, 3.30])
plt.title('Distribuzione massa invariante')
plt.xlabel('Massa invariante (GeV)')
plt.show()

bincenter1 = (bins1[1:] + bins1[:-1]) / 2

#fit 
def fg1(x, A, mu, sigma, p0, p1):
    return A * np.power(np.e, -(pow(x-mu, 2)) / (2*sigma**2)) + p1*x + p0

def fg2(x, A1, A2, mu, sigma1, sigma2, p0, p1):
    return A1 * np.power(np.e, -(pow(x-mu, 2)) / (2*sigma1**2))  + A2 * np.power(np.e, -(pow(x-mu, 2)) / (2*sigma2**2)) + p1*x + p0 

params1, params_covariance1 = scipy.optimize.curve_fit(fg1, bincenter1, n1, sigma=np.sqrt(n1), absolute_sigma=True)
print(params1)

scart1 = (fg1(bincenter1, params1[0], params1[1], params1[2], params1[3], params1[4]) - n1)
rapp_scart1 = (fg1(bincenter1, params1[0], params1[1], params1[2], params1[3], params1[4]) - n1) / np.sqrt(n1)

fig, axs = plt.subplots(3, 1, gridspec_kw={'height_ratios': [3, 1, 1]}, sharex=True, figsize=(13, 10))
fig.subplots_adjust(hspace=0)
axs[0].set_title('Confronto Dati - Fit (gaussiana singola)')
n1, bins1, patches1 = axs[0].hist(mass, bins=100, range=[2.80, 3.30])
axs[0].plot(bincenter1, fg1(bincenter1, params1[0], params1[1], params1[2], params1[3], params1[4]), color='red')
axs[1].errorbar(bincenter1, scart1, yerr=np.sqrt(n1), fmt='o', color='darkred', label='scarti')
axs[1].legend(fontsize=8)
axs[1].grid()
axs[2].errorbar(bincenter1, rapp_scart1, fmt='o', color='orange', label='scarti normalizzati')
axs[2].legend(fontsize=8)
axs[2].grid()
plt.show()



n2, bins2, patches2 = axs[0].hist(mass, bins=100, range=[2.80, 3.30])
bincenter2 = (bins2[1:] + bins2[:-1]) / 2
params2, params_covariance2 = scipy.optimize.curve_fit(fg2, bincenter2, n2, sigma=np.sqrt(n2), absolute_sigma=True)
print(params2)


fig, axs_2 = plt.subplots(3, 1, gridspec_kw={'height_ratios': [3, 1, 1]}, sharex=True, figsize=(13, 10))
fig.subplots_adjust(hspace=0)
axs_2[0].set_title('Confronto Dati - Fit (gaussiana doppia)')
n2, bins2, patches2 = axs_2[0].hist(mass, bins=100, range=[2.80, 3.30])
axs_2[0].plot(bincenter2, fg2(bincenter2, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6]), color='red')
scart2 = (n2 - fg2(bincenter2, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6]))
rapp_scart2 = scart2 / np.sqrt(n2)
axs_2[1].errorbar(bincenter2, scart2, yerr=np.sqrt(n2), fmt='o', color='darkred', label='scarti')
axs_2[1].legend(fontsize=8)
axs_2[1].grid()
axs_2[2].errorbar(bincenter2, rapp_scart2, fmt='o', color='orange', label='scarti normalizzati')
axs_2[2].legend(fontsize=8)
axs_2[2].grid()
plt.show()

#confronto fit 
fig, ax = plt.subplots(figsize=(13, 10))
plt.title('Confronto tra i due fit')
n1, bins1, patches1 = plt.hist(mass, bins=100, range=[2.80, 3.30], alpha=0.7, color='orange')
plt.plot(bincenter2, fg2(bincenter2, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6]), color='red', label='Gaussiana doppia')
plt.plot(bincenter1, fg1(bincenter1, params1[0], params1[1], params1[2], params1[3], params1[4]), color='royalblue', label='Guassiana singola')
plt.xlabel('Massa invariante (GeV)')
plt.legend(fontsize=10)
plt.show()

#confronto scarti
plt.errorbar(bincenter2, rapp_scart2, fmt='o', color='darkred', label='scarti gaussiana doppia', alpha=0.7)
plt.errorbar(bincenter1, rapp_scart1, fmt='o', color='orange', label='scarti gaussiana singola')
plt.legend(fontsize=8)
plt.grid()
plt.show()


scart1_2 = np.power(scart1, 2)
expect1 = fg1(bincenter1, params1[0], params1[1], params1[2], params1[3], params1[4])
chi2_1 = np.sum(scart1_2 / expect1)
chi2_1r = chi2_1 / 95

scart2_2 = np.power(scart2, 2)
expect2 = fg2(bincenter2, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6])
chi2_2 = np.sum(scart1_2 / expect2)
chi2_2r = chi2_2 / 93
print('Chi2 singola gaussiana: ', chi2_1)
print('Chi2 doppia gaussiana: ', chi2_2)
print('Chi2 ridotto singola gaussiana:', chi2_1r)
print('Chi2 ridotto doppia gaussiana: ', chi2_2r)
