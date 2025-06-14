# Control Statements in Python
# 1. Conditional Statements -> if, elif, else
# 2. Looping Statements -> for, while
# 3. Control Transfer Statements -> break, continue, pass

"""Conditional Statements
 if Condition:
      Code to execute if condition is true
 elif Condition:
      Code to execute if the first condition is false and this condition is true
 else:
      Code to execute if all conditions are false"""


from operator import contains


x = 10
if x > 0:
    print("x is Positive Number")
else:
    print("X is not a Postitve Number")
    
# Exercise - Given a number, verify that the number is a multiple of 2 or not
number = int(input("Enter the Number: "))
if number % 2 == 0:
    print("Number is Multiple of 2")
else:
    print("Number is not a Multiple of 2")
    
# Exercise - following dictionary, check if the key exists or not key to check is 'b'
my_dict = {'a':1,'b':2,'c':3}
if 'b' in my_dict:
    print("Key 'b' is present")
else:
    print("key 'b'is not present")
    

a = 10
b = 20
c = 30
if a > b and a > c:
    print("a is greater than b and c")
elif b > a and b > c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")
    
# Nested if statements
x = 10
y = 20
if x > 0:
    print("x is Positive Number")
    if y > 0:
        print("y is also Positive Number")
        
        
age = 25
income = 50000
if age >= 18:
    print("Eligible to vote")
    if income >= 30000:
        print("Eligible for loan")
    elif income >= 20000:
        print("Eligible for credit card")
    else:
        print("Not eligible for loan or credit card")
        
else: 
    print("Not eligible to vote")
    
#shorthand if statement
text = "Hello Python"
contains_python = True if "Python" in text else False
print(contains_python)

score = 85
grade = 'A' if score >= 90 else('B' if score >= 80 else('C' if score >= 70 else 'D'))
print(f"Your grade is: {grade}")


 