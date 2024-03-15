#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
N1, N2 = None, None

if number < 0:
    N1, N2 = -1 * (abs(number) % 10), number % 10
    print(f"Last digit of {number} is {N1}", end="")
else:
    N2 = number % 10
    print(f"Last digit of {number} is {N2}", end="")

if N2 > 5:
    print(" and is greater than 5")
elif N2 == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
