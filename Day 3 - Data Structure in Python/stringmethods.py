string1 = "apple"
string2 = "banana"

print(string1 == string2) # Check if string1 is equal to string2
print(string1 != string2) # Check if string1 is not equal to string2
print(string1 < string2)  # Check if string1 is less than string2   
print(string1 > string2)  # Check if string1 is greater than string2
print(string1 <= string2) # Check if string1 is greater than or equal to string2    
print(string1 >= string2) # Check if string1 is less than or equal to string2

print(ord('a')) # Get the ASCII value of 'a'

print("cat" < "catalog") # Check if "cat" is less than "catalog" # True

print("zebra" < "apple") # Check if "zebra" is less than "apple" # False

#replace() method
# The replace() method replaces a specified phrase with another specified phrase in a string.
string = "Hello, World!"
new_string = string.replace("World", "Python")
print(new_string) # Output: Hello, Python!

#split() method
# The split() method splits a string into a list.
# The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
string = "apple,banana,cherry"
fruits = string.split(",")
print(fruits) # Output: ['apple', 'banana', 'cherry']

# format() method
# The format() method formats specified values in a string.
age = 36
txt = f"My name is John, and I am {age}"
print(txt) # Output: My name is John, and I am 36 
#another way to format string
txt = "My name is John, and I am {}".format(age)
print(txt) # Output: My name is John, and I am 36
#another way to format string
txt = "My name is John, and I am {}"
print(txt.format(age)) # Output: My name is John, and I am 36

#strip() method
# The strip() method removes any whitespace from the beginning or the end of a string.
string = "   Hello, World!   "
new_string = string.strip()
print(new_string) # Output: Hello, World!

#lstrip() method
# The rstrip() method removes any whitespace from the end of a string.
string = "   Hello, World!   "
new_string = string.rstrip()
print(new_string) # Output:    Hello, World!

#rstrip() method
# The lstrip() method removes any whitespace from the beginning of a string.    
string = "   Hello, World!   "
new_string = string.lstrip()
print(new_string) # Output: Hello, World!

#index() method
# The index() method finds the first occurrence of the specified value.
# It raises an exception if the value is not found.
string = "Hello, welcome to my world."
index = string.index("welcome")
print(index) # Output: 7

#find() method
# The find() method finds the first occurrence of the specified value.
# It returns -1 if the value is not found.
string = "Hello, welcome to my world."
index = string.find("welcome")
print(index) # Output: 7

#count() method
# The count() method returns the number of times a specified value occurs in a string.
sentence = "The quick brown fox jumps over the lazy dog."
count = sentence.count("ro")
print(count) # Output: 1

#isalpha() method
# The isalpha() method returns True if all characters in the text are letters (a-z).
# Example 1: Check if all characters are letters
string = "HelloWorld"
print(string.isalpha()) # Output: True

#isdigit() method
# The isdigit() method returns True if all characters in the text are digits (0-9).
isdigit_string = "123456"
print(isdigit_string.isdigit()) # Output: True

#isalnum() method
# The isalnum() method returns True if all characters in the text are alphanumeric (a-z, A-Z, 0-9).
alnum_string = "Hello123"
print(alnum_string.isalnum()) # Output: True

#isupper() method
# The isupper() method returns True if all characters in the text are upper case.
upper_string = "HELLO"
print(upper_string.isupper()) # Output: True

#islower() method
# The islower() method returns True if all characters in the text are lower case.
lower_string = "hello"
print(lower_string.islower()) # Output: True

#istitle() method
# The istitle() method returns True if the string follows the rules of a title.
title_string = "Hello World"
print(title_string.istitle()) # Output: True

#swappecase() method
# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
string = "Hello World"
swapped_string = string.swapcase()
print(swapped_string) # Output: hELLO wORLD

