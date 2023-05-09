print('1)')
list = [int(input(f'Enter number #{i}: ')) for i in range(1,5+1)]
print(list)

print('2)')
A = [1, 2, 3, 4, 5]
A.pop()
print(A)

print('3)')
A = [int(input(f'Enter number #{i}: ')) for i in range(1,10+1)]
N = int(input('Enter number to search: '))
x=0
for i in A:
    if i == N:
        x += 1
print(A.count(N))

print('4)')
N = int(input('Enter the total number of digits: '))
A = [int(input(f'Enter number #{i}: ')) for i in range(1,N+1)]
A.reverse()
print(A)

print('5)')
A = [int(input(f'Enter number #{i}: ')) for i in range(1,5+1)]
C = [i for i in A if i > 5]
print(C)

print('6)')
N = int(input('Enter the total number of digits: '))
A = [int(input(f'Enter number #{i}: ')) for i in range(1,N+1)]
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

