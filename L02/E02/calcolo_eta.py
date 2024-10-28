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
age = date_now - my_date

print('-- Età --')
print('Giorni: ', age.days)
print('Secondi: ', age.seconds)
print('Microseconds: ', age.microseconds)

age_seconds = age.total_seconds()
print('Età in secondi: ', age_seconds)

age_days = age.days
print('Età in giorni: ', age_days)

age_years = date_now.year - my_date.year
print('Età in anni: ', age_years)