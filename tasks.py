print('1)')
word = input('Enter your word: ')
print('+' if word == word[::-1] else '-')

print('2)')
text = input('Enter your text:')
word = input('Enter your word:')
print('Yes' if word in text else 'No')

print('3)')
text = input('Enter your text: ')
if 'abc' in text[0:3]:
    print(text.replace('abc', 'www'))
else:
    print(text+'qqq')

print('4)')
text = input("Enter your text: ")
digits = "0123456789"
no_dig_text = ""
for i in text:
    if i not in digits:
        no_dig_text += i
print(no_dig_text)

print('5)')
email = input('Enter email:')
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')
