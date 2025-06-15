# Function 
# Function is a block of code that only runs when it is called.

# Function Definition or Function Declaration
# Function is defined using the def keyword, followed by the function name and parentheses.
from os import name
from unittest import result


def greet(name):
    print(f"Hello, {name}")
    
# Function Call
## To execute the function, you call it by its name followed by parentheses.
greet("Mohit") # This will call the function and print "Hello, Mohit"

# Built-in Functions
# Python provides many built-in functions that you can use directly.
# For Example, the print() function is a built-in function that outputs text to the console.

# User-Defined Functions
# You can create your own functions to perform specific tasks.

def myfunction(*learners):
    print("One of the learners is: ", learners[2])

myfunction("Mohit", "Rohit", "Sohit", "Tohit")


# Function with Default Parameter
# You can define a function with default parameters, which will be used if no argument is provided.
def my_function(Country = "India"):
    print("I am from " + Country)

my_function("USA")  # This will print "I am from USA"
my_function()  # This will print "I am from India" since the default value is used


def function(a, b, c = 10): # def function(a, b=10, c): This will raise an error because 'c' is a required parameter without a default value
    return a + b - c

result = function(5, 3)
print(result)  


def cal(x, y, w=1, z=2):
    return x + y + w + z    

res= cal(1, 2, z=4) # This will call the function with x=1, y=2, w=1 (default), z=4
print(res)  # Output: 8


def sum_and_product(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result
# This function returns both the sum and product of two numbers
num1 = 10
num2 = 20
sum_result, product_result = sum_and_product(num1, num2)
print(sum_result)  # Output: 30
print(product_result)  # Output: 200

# Nested Functions
def calcu(x,y):
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b
    
    def calculate(op, a, b):
        if op == 'add':
            return add(a, b)
        elif op == 'sub':
            return sub(a, b)
        elif op == 'mul':
            return mul(a, b)
        else:
            return "Invalid operation"
    return calculate('add',x, y), calculate('sub',x, y), calculate('mul',x, y)

result = calcu(5, 3)  # This will call the nested function to add 5 and 3
print(result)  # Output: (8, 2, 15)


def print_args(*args):
    for arg in args:
        print(arg)
print_args(10, 20, 30)


def print_kwargs(**kwargs):
    for key,  value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Mohit", age=18, city="Nashik")


# Recursion is a programming technique where a function calls itself to solve a problem.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_result = factorial(5)  # This will calculate the factorial of 5
print(factorial_result)  # Output: 120


# Lambda Functions
# Lambda functions are small anonymous functions defined using the lambda keyword.
# Syntax: lambda arguments: expression
add = lambda x,y : x + y
print(add(5, 3))   

square = lambda x : x ** 2
print(square(4))  # Output: 16

learner = {
    'Mohit' : 96,
    'Rohit' : 98,
    'Sohit' : 99,
    'Tohit' : 97
}

sorted_values = dict(sorted(learner.items), key = lambda items: items[1])
print(sorted_values)  # This will sort the dictionary by values in ascending order.
