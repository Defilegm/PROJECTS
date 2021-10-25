duration = int(input('Введите продолжительность времени в секундах: '))
time =[]

if duration < 60:
    time.append(f'{duration} cек')

if duration < 3600 and duration >= 60:
    time.append(f'{duration // 60}  мин {duration % 60} сек')

if   duration < 86400 and duration >= 3600:
    time.append(f'{duration // 3600} час {duration % 3600 // 60} мин {duration % 3600 % 60} cек')

if duration >= 86400:
    time.append(
        f'{duration // 86400} дн {duration % 86400 // 3600} час {duration % 86400 % 3600 // 60} мин {duration % 86400 % 60} cек')
print(time)
