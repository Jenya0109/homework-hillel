n=int(input('Введіть число:'))
i = 1
for i in range(n+1):
   while i % 3 == 0:
       print(i)
       i += 1

n=int(input('Введіть число:'))
s = 0
for i in range(n+1):
    while i % 3 == 0:
        s += i
        i += 1
print(s)
