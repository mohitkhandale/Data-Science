 # Modules are files containing Python code (functions, classes, variables) that can be imported and reused in other Python programs. 
 # They help organize code into separate files for better structure and maintainability.
 # Modules are useful in reusability of a code in python
 # Modules means Library
 # Types of Module : 1) User Defined Module, 2) Built in Module (ex. Math, Numpy, Pandas)

import modCalculator as calc
import string_utils  as sttr

# Factorial of the number
fact_result = calc.factorial(11)
print(f"The factorial of 11 is: {fact_result}")

# Squared of the number
square_result = calc.square(5)
print(f"The Squared of 5 is: {square_result}")

# Cube of the Number
cube_result = calc.cube(5) 
print(f"The Cube of 5 is: {cube_result}")

# reversal of the string
String_revesal = sttr.reverse("Hello")
print(f"Reversal of Given String is: {String_revesal}")

# Concatenation of the string
String_con = sttr.concatenation("Hello", "World")
print(f"The Concatenation of Given string is: {String_con}")

# Palidrome of the string
String_palidrome = sttr.palidrome("madam")
print(String_palidrome)

# Length of the string
String_length = sttr.length("Hello")
print(f"Length of the String is: {String_length}")

# importing Specific method from a library or a module
from string_utils import concatenation 
concatenate = concatenation("Hello", "World")
print(f"The Concatenation of Given string is: {concatenate}")

import datetime
today = datetime.date.today()
print(f"Today's date is: {today}")

now = datetime.datetime.now()
print(f"Today's timestamp is: {now}")


import random
print(random.randint(1,10))
print(random.uniform(1,10))
print(random.choice(['apple','banana','cherry']))