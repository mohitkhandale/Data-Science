""" File Handling:
- File handling refers to the process of reading from and writing to files using a programming language.
- In Python, file handling allows you to create, read, update, and delete files on your system.
- Common file operations include opening a file, reading its contents, writing data, and closing the file."""

# Reading a file
file = open('E:\Data Science\Phase 0 - Python\Day 8 - Modules & File Handling in Python\myinfo.txt','r') # Opens the file 'myinfo.txt' located at the specified path in read mode ('r').
content = file.read() # Reads the entire content of the file and stores it in the variable 'content'.
print(content)
print(file.read(6)) # Attempts to read the next 6 characters from the file (will return an empty string if the file pointer is at the end).
print(file.readline()) # Reads and prints the next line from the file (will return an empty string if the file pointer is at the end).
print(file.readlines()) # Reads and prints all remaining lines from the file as a list (will return an empty list if the file pointer is at the end).
file.close() # # Close the file to free up system resources


try:
    file = open('E:\Data Science\Phase 0 - Python\Day 8 - Modules & File Handling in Python\myinfo.txt','r') # Opens the file 'myinfo.txt' located at the specified path in read mode ('r').
except Exception as e:
    print(f"An error occurred: {e}")
else:
    content = file.read() # Reads the entire content of the file and stores it in the variable 'content'.
    print(content)
finally:
    try:
        file.close()
    except:
        pass
    
# Writing a file
# Write method returns the number of characters written to the file. 
try:
    file = open('E:\Data Science\Phase 0 - Python\Day 8 - Modules & File Handling in Python\myinfo.txt','w') # Opens the file 'myinfo.txt' located at the specified path in write mode ('w').
except Exception as e:
    print(f"An error occurred: {e}")
else:
    content = file.write("My self Mohit Deepak Khandale") # Writes the entire content of the file and stores it in the variable 'content'.
    print(content)
finally:
    try:
        file.close()
    except:
        pass
    
# Appending into existing file
# Adding Content in the file
try:
    file = open('E:\Data Science\Phase 0 - Python\Day 8 - Modules & File Handling in Python\myinfo.txt','a') # Opens the file 'myinfo.txt' located at the specified path in append mode ('a').
except Exception as e:
    print(f"An error occurred: {e}")
else:
    content = file.write("My self Mohit Deepak Khandale") # Writes the entire content of the file and stores it in the variable 'content'.
    print(content)
finally:
    try:
        file.close()
    except:
        pass

# Exclusive File handling 'x' 
# Creates a file and wrutes the content in it 

try:
    file = open('E:\Data Science\Phase 0 - Python\Day 8 - Modules & File Handling in Python\mytype.txt','x') # Creating the file 'mytype.txt' located at the specified path in Exclusive mode ('x').
    file.write("My self Mohit Deepak Khandale")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    file.close()
    file = open('E:\Data Science\Phase 0 - Python\Day 8 - Modules & File Handling in Python\mytype.txt','r')
    contents = file.read()
    print(contents)
finally:
    try:
        file.close()
    except:
        pass