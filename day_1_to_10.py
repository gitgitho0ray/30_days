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

print(i+int(input()))
print(d + float(input()))
print(s + str(input()))

### DAY_2 ###

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tips=meal_cost*tip_percent/100
    tax=meal_cost*tax_percent/100
    total = meal_cost+tips+tax
    return total

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)

print(round(solve(meal_cost, tip_percent, tax_percent)))

### DAY_3 ###
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())


if N % 2 == 0:
    if N in range(2,6):
        print('Not Weird')
    elif N in range (6,21):
        print('Weird')
    elif N > 20:
        print('Not Weird')
else:
    print('Weird')




### DAY_4 ###
### DAY_5 ###
### DAY_6 ###
### DAY_7 ###
### DAY_8 ###
### DAY_9 ###

