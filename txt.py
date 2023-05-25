print('1)')
numbers = []
with open ('text_file.txt') as f:
    text_file = f.read()
    text_file = text_file.split()
    for number in text_file:
        if number.isdigit():
            numbers.append(number)
print(numbers)

print('2)')
text = input('Enter your text: ')
with open('data.txt', 'w') as f:
    f.write(text)

print('3)')
N = int(input('Enter the total number of digits: '))
numbers = []
for i in range(N):
    digits = input(f'Enter your numbers {i+1}: ')
    numbers.append(digits)
with open('numbers.txt', 'w') as f:
    f.write(' '.join(numbers))

print('4)')
import random
numbers = []
for digits in range(100):
    numbers.append(str(random.randint(1, 1000)))
with open('random_numbers.txt', 'w') as f:
    f.write('\n'.join(numbers))

print('5)')
with open('words.txt', 'r') as f:
    words_text = f.read()
    words = words_text.split()
print(f'The total number of words in the file "words.text": {len(words)}')

print('6)')
with open('total_number.txt', 'r') as f:
    total = []
    for numbers in f:
        for number in numbers.split():
            if number.isdigit():
                total.append(int(number))
print(f'The total number of digits in the file "total_number.txt": {sum(total)}')

print('7)')
from collections import Counter
with open('common.txt', 'r') as f:
    text = f.read()
words = text.split()
words_counts = Counter(words)
common_words = words_counts.most_common(5)
print('The most common words in the file "common.txt":')
for word, count in common_words:
    print(f'"{word}" - {count}')
