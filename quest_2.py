cubenumber = []
result = 0
for i in range (1,1000,2):
     i = i ** 3
     cubenumber.append(i)

for i in cubenumber:
     summ = [int(a) for a in str(i)]
     x = sum(summ)
     if x % 7 == 0:
          result += i
print(result)

result = 0
for i in cubenumber:
     i+=17
     summ = [int(a) for a in str(i)]
     x = sum(summ)
     if x % 7 == 0:
          result += i

print(result)