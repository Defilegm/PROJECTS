for n in range(1,101):
     if n < 21:
          if n == 1:
               print(f'{n} процент')
          elif n == 2 or n == 3 or n  == 4:
               print(f'{n} процента')
          else:
               print(f'{n} процентов')
     if n > 20:
          if n % 10 == 1:
               print(f'{n} процент')
          elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
               print(f'{n} процента')
          else:
               print(f'{n} процентов')