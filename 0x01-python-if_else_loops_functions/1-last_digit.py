#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -last
if last == 0:
    msg = "and is 0"
elif last > 5:
    msg = "and is greater than 5"
elif 0 < last < 6:
    msg = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {msg}")
