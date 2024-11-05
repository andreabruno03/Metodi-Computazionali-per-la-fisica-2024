import somme

res1 = somme.somma(2)
res2 = somme.somma_sqrt(2)

print('Risultato somma dei primi 10 numeri naturali: ', res1)
print('Risultato somma delle radici dei primi 10 numeri naturali: ', res2)

res3 = somme.sommaprod(2)
print('Somma: ', res3[0], "\n Prodotto: ", res3[1])

res_sum = somme.sommatoria(2, 0.5)
print(res_sum)