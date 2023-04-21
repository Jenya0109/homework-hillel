import math

a=int(input('Enter first side:'))
b=int(input('Enter second side:'))
c=int(input('Enter third side:'))

p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))

print(s)
