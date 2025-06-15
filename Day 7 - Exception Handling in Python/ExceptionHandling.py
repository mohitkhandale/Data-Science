"""
Exception Handling is a mechanism in Python that allows you to handle errors gracefully without crashing the program. 
It involves using `try`, `except`, `else`, and `finally` blocks to catch and manage exceptions.  
- Types  of Errors:
1. Syntax Errors: These occur when the code is not written correctly, such as missing colons or parentheses.
2. Logical Errors: These occur when the code runs without crashing but produces incorrect results.
3. Runtime Errors: These occur during the execution of the program, such as division by zero or accessing an undefined variable.

try block: This block contains the code that may raise an exception. If an exception occurs, the code in the `except` block is executed.
except block: This block is executed if an exception occurs in the `try` block. You can specify the type of exception you want to catch.
else block: This block is executed if no exceptions occur in the `try` block. It is useful for code that should run only if the `try` block is successful.
finally block: This block is always executed, regardless of whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.  
"""

try:
    num = int(input("Enter a number: ")) # This may raise a ValueError if the input is not a valid integer
    result = 10 / num
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") # This will catch division by zero errors
except:
    print("An unexpected error occurred.")
else:
    print(f"The result is: {result}") # This will execute if no exceptions occur
finally:
    print("Execution completed.") # This will always execute, regardless of whether an exception occurred or not
# Example of handling multiple exceptions


try:
    my_list = [1,2,3,4,5,6,7,8]
    index = int(input("Enter an index to access the list: ")) # This may raise a ValueError if the input is not a valid integer
except IndexError:
    print("Error: Index out of range. Please enter a valid index.")
else:
    print(f"The value at index {index} is: {my_list[index]}")   
finally:
    print("List access attempt completed.")


my_dict = {'name': 'Mohit', 'age': 20, 'city': 'Delhi'}
executed = False
try:
    key = input("Enter a key to access the dictionary: ") # This may raise a KeyError if the key does not exist
    value = my_dict[key]
    executed = True
except KeyError:
    print(f"Error: The key '{key}' does not exist in the dictionary.")
else:
    print(f"The value for the key '{key}' is: {value}")
finally:
    if executed:
        print("Dictionary access was successful.")
    else:
        print("Dictionary access failed.")
    
# raise Exception
# This is used to raise an exception manually. It can be used to create custom exceptions or to re-raise an existing exception.
x = 10
if x > 5:
    raise Exception("x should not be greater than 5")  # This will raise an exception with the specified message
    
    