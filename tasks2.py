print('1)')
list = []
for i in range (5):
    numbers = int(input('Enter you number: '))
    list.append(numbers)
print(list)

print('2)')
A = [1, 2, 3, 4, 5]
A.pop()
print(A)

print('3)')
A = []
for i in range (10):
    numbers = int(input('Enter you number: '))
    A.append(numbers)
N = int(input('Enter number to search: '))
x=0
for i in A:
    if i == N:
        x += 1
print(A.count(N))

print('4)')

N = int(input('Enter the total number of digits: '))
A = []
for i in range(N):
    numbers = int(input('Enter your number: '))
    A.append(numbers)
A.reverse()
print(A)

print('5)')
A = []
for i in range(5):
    numbers = int(input('Enter you number: '))
    A.append(numbers)
C = []
for numbers in A:
    if numbers > 5:
        C.append(numbers)
print(C)

print('6)')
N = int(input('Enter the total number of digits: '))
A = []
for i in range(N):
    numbers = int(input('Enter your number: '))
    A.append(numbers)
min = A[0]
max = A[0]
for i in A:
    if i > max:
        max = i
    if i < min:
        min = i
print(f'Your max number in the list {max} and your min number in the list {min}')

print('7)')
text = input('Enter your text: ')
x = 0
for i in text:
    if i.isdigit():
        x += 1
print(f'{x} digits in your text')

