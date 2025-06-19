# This file is working as a module where all the required function are defined 
def square(num):
    return num*num

def cube(num):
    return num ** 3

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

def add(num1 , num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    if num2 == 0:
        return "Cannot Divide By Zero"
    else:
        return num1 / num2

def module(num1 , num2):
    return num1 % num2

