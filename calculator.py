import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a + b

def sub(a, b):
    a - b

def mul(a, b):
    a * b

# Divides b by a (b/a)
def div(a, b):
    try:
        return b/a
    except ZeroDivisionError:
        return("Can't divide by zero!")

def log(a, b):
    try:
        math.log(a, b)
    except ValueError:
        print("Can't take the logorithm of a negative number!")

def exp(a, b):
    return math.pow(a, b)



