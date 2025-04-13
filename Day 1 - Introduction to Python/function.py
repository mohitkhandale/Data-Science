# print() function -> display the output to the screen
print("Hello World")

# By default, the print() function adds a new line after each print statement.
print("Hello")
print("World")

# To avoid this, we can use the end parameter to specify what to print at the end of the output.
print("Hello", end= " ")
print("World")

# 'sep' Parameter
print("apple","banana","orange")

#sep parameter is used to specify the separator between the values.
print("apple","banana","orange", sep= ", ")

# input() function -> takes input from the user and returns it as a string.
user_input =  input("Enter your name: ")
print("Hey", user_input) 
print("Hey" + user_input)

user_input =  "Rohit Khandale"
print(user_input)

'''
multi-line comments
multi-line comments are written inside triple quotes.
multi-line comments are not executed by the interpreter.
multi-line comments are used to write documentation for the code.
multi-line comments are used to write notes for the code.
'''

# Intentation -> Indentation is used to define the scope of the code.
# Intentation: structure of the code block.
x = 10
if x > 5:
    print("x is greater than 5")
# IndentationError: unexpected indent -> This error occurs when there is an unexpected indent in the code.

# variables -> Container that hold the data
# LEGAL VARIABLES NAME ->
# 1. Variable name should start with a letter or underscore.
# 2. Variable name can contain letters, numbers, and underscores.   
# Case sensitive -> Variable names are case sensitive.
# 3. Variable names should not be a reserved keyword in Python.
# 4. Variable names should not contain spaces.
# 5. Variable names should not start with a number.
# 6. Variable names should be in lowercase letters.

# Data Types: Nature of the data that any variable can hold.
# 1. int -> Integer (whole number)
x = 10
print(type(x))

# 2. float -> Floating point number (decimal number)
y = 10.5
print(type(y))

# 3. str -> String (text data)
name = "Mohit Khandale"
print(type(name))

# 4. bool -> Boolean (True or False)
is_student = True
print(type(is_student))

# 5. list -> List (ordered collection of items)
my_list = [1, 2, 3, 4, 5]
print(type(my_list))

# 6. tuple -> Tuple (ordered collection of items, immutable)
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))

# 7. set -> Set (unordered collection of unique items)
my_set = {1, 2, 3, 4, 5}
print(type(my_set))

# 8. dict -> Dictionary (unordered collection of key-value pairs)
my_dict = {"name": "Mohit", "age": 20}
print(type(my_dict))

# 9. None -> NoneType (represents the absence of a value)
my_none = None
print(type(my_none))

# 10. complex -> Complex number (a + bj)
complex_num = 1 + 2j
print(type(complex_num))

# 11. bytes -> Immutable sequence of bytes
byte_data = b"Hello"
print(type(byte_data))

# 12. bytearray -> Mutable sequence of bytes
byte_array_data = bytearray(b"Hello")
print(type(byte_array_data))
