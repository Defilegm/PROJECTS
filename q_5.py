
price_list =[66.72, 17.05, 94.15, 67.51, 89.5, 68.93, 76.02, 61.16, 10.27, 78.23]
i = 0
price_str =''

for price in price_list:
    price_str += f'{int(price)}руб {int(price*100)%100}коп'
    if price_list.index(price) < 9:
        price_str += ', '

print(price_list)
print('список цен: ',price_str)

print('ID списка до сортировки: ', id(price_list))
price_list.sort()
print('Список по ВОЗРАСТАНИЮ : ', price_list)
print('ID списка после сортировки: ',id(price_list))

print('Список цены по УБЫВАНИЮ: ', price_list[::-1])
print('ID списка после сортировки: ',id(price_list))
print('5 самых дорогих товаров по возрастанию: ', price_list[-4::])

