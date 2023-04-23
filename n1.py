import math
import os
import random
import re
import sys

n = int(input('Enter your number: '))

if n % 2 !=0 and n < 20:
    print('Weird')
else:
    if n in range (2, 5):
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    elif n % 2 !=0 and n > 20:
        print('Not Weird')

exit()
