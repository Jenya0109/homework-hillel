import string

s=0
result = True
space = ['+','-','/','@']

password = input('Enter your password:')

if not len(password) >= 8:
    print('The minimum password length is 8.')
else:
    s+=1
    result = False

if not any(char.isdigit() for char in password):
    print('Use digits.')
else:
    s+=1
    result = False

if not any(char.isupper() for char in password):
    print('Use capital letters.')
else:
    s+=1
    result = False

if not any(char.islower() for char in password):
    print('Use small letters.')
else:
    s +=1
    result = False

if not any(char in space for char in password):
    print('Use characters.')
else:
    s+=1
    result = False
print('Your password score:', s ,)


