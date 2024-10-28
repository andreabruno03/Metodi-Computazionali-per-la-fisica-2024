from datetime import datetime, timedelta

data = input('Inserisci la tua data di nascita: ')

print(datetime.now())

my_date = datetime.strptime(data, "%d-%m-%Y %H:%M:%S")
print('Data di nascita inserita: ', my_date)

#stampo separatamente giorno, mese, anno e orario
print('Anno: ', my_date.year)
print('Mese: ', my_date.month)
print('Giorno: ', my_date.day)
print('Ore: ', my_date.hour)

#calcolo età 
date_now = datetime.now()


scelta = input('Scegli unità di misura: ')
def eta(data):
    if scelta == 'anni':
        anni = date_now.year - data.year
        print('Età in anni: ', anni)
    if scelta == 'giorni':
        age = date_now - data
        giorni = age.days
        print('Età in giorni: ', giorni)
    if scelta == 'secondi':
        secondi = age.total_seconds()
        print('Età in secondi: ', secondi)
    if scelta == 'secoli':
        secoli = (date_now.year - data.year) / 100
        print('Età in secoli: ', secoli)

eta(my_date)
