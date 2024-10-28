week = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']

ottobre = week[1:7] + 3*week + week[0:4]


mese = {i : ottobre[i-1] for i in range(1, 32)}
for i in mese:
    if mese[i] == 'domenica':
        print(i , mese[i] , '\n')
    else:
        print(i, mese[i], end=' ')



