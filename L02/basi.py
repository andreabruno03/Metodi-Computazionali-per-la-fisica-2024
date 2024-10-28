# in python non si possono creare variabili senza assegnarli un valore
s = 'questa è una stringa'
s_1 = 'Anche '
ss = s_1 + s
print(ss)

#booleani
vc1 = (10 > 5) #sto chiedendo se è vera la condizione tra parentesi
print(vc1)

#variabile senza valore
v = None
print(type(v))
#questo permette di avere una variabile che si adattera a quello che serve nel codice

#richiesta di input
nn = input('Immettere  un numero: ')
print('Il numero inserito: ', nn)

nn = int(nn)
somma = nn + 10
print('il numero sommato a 10 è ', somma)

#le liste sono alla base di python
lista = ['a', 'b', 'c', 'd']
print(lista)

lunghezza = len(lista)

#per la funzione range il primo valore è incluso mentre l'altro è escluso
for j in range(2, 10):
    print(j)

check = 0
while check < 5:
    check = check + 1 
    print(check)

#entra nella codice dell'if solo se la condizione si trova ad essere vera
n = 2
if n < 5:
    print('Giusto')
elif n > 1:
    print('Maggiore di 1')
else:
    print('Il numero o è 1 o è maggiore di 5')

#se ho conidizioni logiche multiple
k = 3
if k >= 1 and k < 5:
    print(k)


#formattazione stringhe: programmare la stringa senza sapere il valore delle variabili
pippo = 'pippo'
pluto = 'pluto'
paperino = 'paperino'

sf = 1.35
sg = 0.97
int = 3

mysg = 'Esempio di formattazione generica -->{:} - {:} -- {:}'.format(sg, pippo, sf)
print(mysg)
#in alcuni casi posso specificare il tipo di variabile che mi aspetto
mysg1 = 'Esempio di formattazione con valore specifico -->{:d}'.format(int) #ho richiesto un intero
mysg2 = 'Esempio di formattazione con valore specifico -->{:04d}'.format(int) #lo uso per allineare a destra gli zeri

print(mysg2)

#con i float
mysf = 'Esempio di formattazione con float -->{:f}'.format(sf)
mysf1 = 'Esempio di formattazione con float, specificando numero di cifre dopo la virgola -->{:04f}'.format(sf)

print(mysf)
print(mysf1)

#formatazzione stringhe
ll = ['Pippo', 'Pluto', 'Paperino']
for s in ll:
    print('{:<10} {:02d}'.format(s, int)) #allineo sulla sinistra

for s in ll:
    print('{:^10} {:02d}'.format(s, int)) #allineo al centro



#dizionari
age_dict = {'Pietro' : 33, 'Giulia' : 23, 'Michele' : 44, 'Matilde' : 45}
print(age_dict)
print(age_dict['Pietro']) # mi dà il contenuto associato alla chiave che ho specificato
for k in age_dict:
    print(k) #stampa le chiavi

for k in age_dict:
    print('{:<20} {:d}'.format(k, age_dict[k])) #stampo le chiavi e i valori associati nel dizionario

#funzioni prova
def fprova():
    print('Ciao') #così la definisco soltanto
fprova() # chiama la funzione prova

#funzione che accetta un valore
def prova_input(vi):
    print('La funzione restituisce: {:}'.format(vi))

#funzione che resituisce un valore a partire da più parametri
def restituisci(a, b):
    sum = a + b
    print(sum)

restituisci(3, 2)

#funzione che resistuisce più valori
def powe(b, e):
    v1 = b * e
    v2 = b**2 * e
    v3 = b**2 * e**2
    return v1, v2, v3

a, b, c = powe(1, 3)
print(a, ', ', b, ', ', c)

#posso anche definire una sola variabile ma poi avrò un oggetto composto in output
res = powe(1, 3)
print(res)

