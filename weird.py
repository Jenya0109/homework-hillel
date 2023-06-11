number = int(input('Enter your number: '))
n = number % 2
if n == 1 and number > 20:
    print('Not Weird')
elif n == 0 and 2 <= number <= 5:
    print('Not Weird')
elif n == 0 and 6 <= number <= 20:
    print('Weird')
elif n == 1:
    print('Weird')