#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# stringify the number
num_str = repr(number)
last = num_str[-1]

# start printing script
print("Last digit of", number, "is ", end='')

# check if @number is negative
if number < 0:
        if last != 0:
                print("-", end='')

print(last, end='')

# finer specifications
if last > '5':
        if number > 0:
                print(" and is greater than 5")

elif last == '0':
        print(" and is 0")

else:
        print(" and is less than 6 and not 0")
