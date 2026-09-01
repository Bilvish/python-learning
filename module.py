# Built-in module
import math

print(math.sqrt(25))
print(math.pi)


# Import specific function
from math import factorial

print(factorial(5))


# Import with an alias
import math as m

print(m.pow(2, 3))


# User-defined module
# Suppose calculator.py contains:
#
# def add(a, b):
#     return a + b
#
# We can use it in another file:
#
# import calculator
# print(calculator.add(10, 20))