print('1.')
n = int(input('Введіть ширину трикутника: '))
for i in range(n):
    print('*' * (n - i))

print('2.')
n = int(input('Введіть ширину трикутника: '))
for i in range (n):
    print ('*'*(i+1))

print('3')
n = int(input("Введіть ширину трикутника:"))
for i in range (n):
    print(" "*i+'*'*(n-i))

print('4')
n = int(input("Введіть ширину трикутника:"))
for i in range (n):
    print(" "*(n-i-1)+'*'*(i+1))
