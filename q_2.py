somelist = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
somelist1 = ''
i=0
while i < len(somelist):
    if somelist[i].isdigit() or somelist[i][:1] == '+':
        if somelist[i][:1] == '+':
            somelist[i] = f'+0{somelist[i][1:]}'
        else:
            somelist[i] = somelist[i].zfill(2)
        somelist.insert(i, '"')
        somelist.insert(i + 2, '"')
        i += 2
    i += 1

i = 0
while i < len(somelist):
    if somelist[i] == '"':
        somelist1 += f'{somelist[i]}{somelist[i+1]}{somelist[i+2]} '
        i += 2
    else:
        somelist1 += f'{somelist[i]} '

    i+=1




print(somelist)
print(somelist1)




