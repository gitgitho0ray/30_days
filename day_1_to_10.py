### DAY_0 ###
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)

### DAY_1 ###
i = 4
d = 4.0
s = 'HackerRank '

print(i + int(input()))
print(d + float(input()))
print(s + str(input()))

### DAY_2 ###

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tips = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total = meal_cost + tips + tax
    return total


if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)

print(round(solve(meal_cost, tip_percent, tax_percent)))

### DAY_3 ###
# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

if N % 2 == 0:
    if N in range(2, 6):
        print('Not Weird')
    elif N in range(6, 21):
        print('Weird')
    elif N > 20:
        print('Not Weird')
else:
    print('Weird')


### DAY_4 ###
class Person:
    def __init__(self, initialAge):
        if initialAge >= 0:
            self.initialAge = initialAge
        else:
            self.initialAge = 0
            print('Age is not valid, setting age to 0.')

    def amIOld(self):
        if self.initialAge < 13:
            print('You are young.')
        elif self.initialAge >= 13 and self.initialAge < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        self.initialAge += 1


### DAY_5 ###
# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
for i in range(1, 11):
    print('{number} x {i} = {total}'.format(number=n, i=i, total=n * i))

### DAY_6 ###

import sys

sysinput = [line.strip() for line in sys.stdin]
for word in sysinput[1:]:
    print(word[0::2], word[1::2])

### DAY_7 ###
# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

print(' '.join([str(i) for i in arr[::-1]]))
### DAY_8 ###
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = [line.strip() for line in sys.stdin]
test = [i for i in data[int(data[0]) + 1:]]
callbook = {i[0]: i[1] for i in [tuple(i.split()) for i in data[1:int(data[0]) + 1]]}
for name in test:
    if name in callbook.keys():
        print(name + '=' + callbook[name])
    else:
        print('Not found')

### DAY_9 ###
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
