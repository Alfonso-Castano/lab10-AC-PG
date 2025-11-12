"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math
#math functions

def add(a, b): 
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    try:
        return b/a
    except ZeroDivisionError:
        print("Can't divide by zero")

def log(a, b):
    try:
        return math.log(b , a)
    except ValueError:
        print("Can't take the logarithm of a negative number")

def exp(a, b):
    return a ** b