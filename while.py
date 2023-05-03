n=int(input('Введіть число:'))
i=0
sum=0
while i <= n:
    if i % 3 == 0:
        sum+= i
        print(i)
    i += 1
print('Summa:', sum)
