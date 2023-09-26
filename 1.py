#Fuctions
import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Немає такої операції."
    return x / y

def exponentiation(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def cube_root(x):
    return x ** (1/3)