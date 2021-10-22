somelist = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i = 0
name = ''
while i < len(somelist):
    for elem in somelist[i][::-1]:
        if elem == ' ':
            break
        name += elem

    i+=1
    name += ' '

name = name[::-1].title()
name = name[1:]
print(f'Имена сотрудников: {name}')
greetings =''
for f in name:
    greetings += f
    if f == ' ':
        print(f'Привет, {greetings}')
        greetings = ''
print(f'Привет, {greetings}')