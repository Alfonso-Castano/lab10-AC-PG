# https://github.com/Alfonso-Castano/lab10-AC-PG.git
#Partner 1: Alfonso Castano
#Partner 2: Pedro Guevera
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math
#math functions
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a+b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm base or argument")
    return math.log(b, a)

def exp(a, b):
    return a ** b