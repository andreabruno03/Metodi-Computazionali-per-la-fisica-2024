import numpy as np

n = input('Inserisci numero naturale: ')
n = int(n)
sum = 0
for i in range(1, n+1):
    sum = sum + i
print('La somma dei primi {:} numeri naturali è '.format(n), sum)
