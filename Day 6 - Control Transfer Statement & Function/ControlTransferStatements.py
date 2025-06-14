# Control Transfer Statements
# Control transfer statements alter the flow of control in a program.
# They can be used to skip certain parts of code, repeat sections, or exit loops and functions.

"""
1. Break Statement 
If the break statement is encountered inside a loop, it immediately terminates the loop.
If the Condition meets, the loop is exited. It will not Explore the remaining iterations.
"""
for i in range(10):
    print(i)
    if i == 5:
        break  # Exit the loop when i is 5

count = 0
while True:
    print("Inside the While Loop")
    count += 1
    if count == 5:
        break  # Exit the loop when count is 5
    
"""
2. Continue Statement
The continue statement skips the current iteration of a loop and moves to the next iteration.
If the Condition meets, the remaining code in the loop is skipped for that iteration.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)  # This will only print odd numbers
    
i = 1
while i < 3:                           
    j = 0
    while j < 5:
        j = j + 1
        if j == 3:
            continue
        print(j)
    i = i + 1  
"""
    i=1                         j=1
                                j=2 
                                j=4
                                j=5
  ------------------------------------                              
    i=2                         j=1
                                j=2 
                                j=4
                                j=5
Output:
1
2
4
5
1
2
4
5
"""   

"""
3. Pass Statement
The pass statement is a null operation; it does nothing when executed.
It is often used as a placeholder in code where a statement is syntactically required but no action is needed.
"""
count = 0
while count < 5:
    pass # Placeholder for future code
    print(count)
    count += 1  # Increment count
    
