#Arithmetic Operators
a = 10
b = 20
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

#Comparison Operators
c = 30
d = 40
print(c == d) # Equal to
print(c != d) # Not equal to
print(c > d) # Greater than
print(c < d) # Less than
print(c >= d) # Greater than or equal to
print(c <= d) # Less than or equal to

#Logical Operators
x = 5
y = 10
z = 15
print(x < y and y < z) # Logical AND
print(x < y or y > z) # Logical OR
print(not(x < y)) # Logical NOT

#Bitwise Operators
a = 10 # 1010 in binary
b = 4 # 0100 in binary
print(a & b) # Bitwise AND
print(a | b) # Bitwise OR
print(a ^ b) # Bitwise XOR
print(~a) # Bitwise NOT
print(a << 2) # Left Shift
print(a >> 2) # Right Shift

#Assignment Operators
a = 10
b = 20
a += b # a = a + b
print(a) # 30
a -= b # a = a - b
print(a) # 10
a *= b # a = a * b
print(a) # 200
a /= b # a = a / b
print(a) # 10.0
a %= b # a = a % b
print(a) # 10.0
a **= b # a = a ** b
print(a) # 100
a //= b # a = a // b
print(a) # 5.0
a &= b # a = a & b
print(a) # 0
a |= b # a = a | b
print(a) # 20
a ^= b # a = a ^ b
print(a) # 0

#Membership Operators
print('a' in 'apple') # True
print('b' not in 'apple') # False
print('a' in ['apple', 'banana', 'cherry']) # True
print('b' not in ['apple', 'banana', 'cherry']) # True

#Identity Operators
a = 10
b = 20
print(a is b) # False
print(a is not b) # True
print([1, 2, 3] is [1, 2, 3]) # False
print([1, 2, 3] is not [1, 2, 3]) # True

print(id(x)) # Memory address of x
print(id(y)) # Memory address of y

#String in Python
name = "Mohit"
type(name) # <class 'str'>

strings = "Hello World"
second_char = strings[1] # 'e'
print(second_char) # e
last_char = strings[-1] # 'd'
print(last_char) # d

#Python Strings are Immutable
# strings[0] = 'h' # TypeError: 'str' object does not support item assignment       

print(len(strings)) # 11 # Length of string

print(strings[0:5]) # Hello # Slicing string
print(strings[6:]) # World # Slicing string
print(strings[:5]) # Hello # Slicing string 
print(strings[1:8:2]) # e Wo # Slicing string
print(strings[::2]) # Hlo ol # Slicing string
print(strings[-4:]) # orld # Slicing string
print(strings[:-5]) # Hello # Slicing string
print(strings[::-1]) # dlroW olleH # Slicing string
print(strings[::]) # Hello World # Slicing string


#Inbuild Functions in String

# String Uppercase
string2 = "hello world"
uppercase_string = string2.upper() # Convert to uppercase
print(uppercase_string) # HELLO WORLD

# String Lowercase
lowercase_string = string2.lower() # Convert to lowercase
print(lowercase_string) # hello world

# String Titlecase
titlecase_string = string2.title() # Convert to titlecase
print(titlecase_string) # Hello World

# String Capitalize
capitalize_string = string2.capitalize() # Convert to capitalize
print(capitalize_string) # Hello world

# String Concatenation
string3 = "hello"
string4 = "world"
concatenated_string = string3 + " " + string4 # Concatenate strings
print(concatenated_string) # hello world

result  = string3 * 3 # Repeat string
print(result) # hellohellohello

