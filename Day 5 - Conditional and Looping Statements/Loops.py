# Loops 
# For Loop
# For loop iterates over a sequence (list, tuple, dictionary, set, or string)
# While Loop
# While loop executes as long as the condition is true

from re import I


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
no = [1,2,3,4,5,6,7,8,9,10]
for i in no:
    if i % 2 == 0:
        print(i, "is even")
    else: 
        print(i, "is odd")
   
        
number = [10, 50, 40, 30, 5, 15]
max_num = number[0]
for num in number:
    if num > max_num:
        max_num = num
        
print("The maximum number is:", max_num)


numbers = [1, 2, 3, 4, 5]
for i in range(3):
    print(numbers[i])
    

for i in range(6):
    print(i)
else:
    print("Loop completed without errors")
    

# List Comprehension
# List Comprehension is used only with lists
# It provides a concise way to create lists
# Syntax: new_list = [expression for item in iterable]
squared_numbers = [x ** 2 for x in range(1,11)]
print("Squared numbers:", squared_numbers)


# Generator Expression
# A Generator Expression is similar to list comprehension but returns a generator object
# It is more memory efficient for large datasets
# Generator Expression is similar to list comprehension but uses parentheses
generator_numbers = (x ** 2 for x in range(1, 11))
print("Generator numbers:")
for num in generator_numbers:
    print(num)
    

# Nested Loops
for i in range(1, 6):
    for j in range(1, 11):
        print(i*j, end='\t')
    print() 
    

# While Loop
count = 1
while count <= 5:
    print("Count is:", count)
    count = count + 1
    
# Nested While Loop
i = 0
while i < 3:
    print("Outer loop iteration:", i)
    j = 0
    while j < 2:
        print("Inner loop iteration:", j)
        j += 1
    i += 1
    
    
# Exercise 1: Find the sum of all even numbers from 1 to 100 using a for loop
sum_even=0
for i in range(1,  101):
    if(i % 2 == 0):
        sum_even = sum_even + i     
print("Sum of even numbers from 1 to 100 is:", sum_even)

# Exercise 2: Write a program to calculate the factorial of a number using a while loop
number = int(input("Enter the number to calculate the factorial: "))
fact = 1
while number > 0:
    fact = fact * number
    number = number - 1
print("The factorial is:", fact)