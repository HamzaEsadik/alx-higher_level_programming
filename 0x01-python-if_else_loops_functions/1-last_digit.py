#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = abs(number) % 10
if number < 0:
    s = -s
print(f"Last s of {number:d} is {s:d} and is ", end="")
if s > 5:
    print("greater than 5")
elif s == 0:
    print("0")
else:
    print("less than 6 and not 0")
