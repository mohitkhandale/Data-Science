my_tuple = (1, 2, 3, 4, 5)# Accessing elements in a tuple
type(my_tuple)

my_tuple[0]  # Accessing the first element

tuple1 =('apple', 123, True, 3.14,[1,2,3])  # Creating a tuple with different data types
print(tuple1)
print(tuple1[-1][1])  # Accessing the second element of the list inside the tuple

print(tuple1[1:4]) # Slicing the tuple to get elements from index 1 to 3 4th element is not included because of slicing rules 

# Tuples are immutable, so we cannot change their elements
# my_tuple[0] = 10  # This will raise a TypeError

print(tuple1[:-1]) # Slicing the tuple to get all elements except the last one
# Tuples can be nested

print(tuple1[::-1]) # Reversing the tuple using slicing

# Built-in Functions 

min_element = min(my_tuple)  # Finding the minimum element in the tuple
max_element = max(my_tuple)  # Finding the maximum element in the tuple
print(f"Minimum element: {min_element}")
print(f"Maximum element: {max_element}")

sum_elements = sum(my_tuple)  # Finding the sum of all elements in the tuple
print(f"Sum of elements: {sum_elements}")

# Converting a tuple to a list
my_list = list(my_tuple)  # Converting tuple to list
print(f"Converted list: {my_list}")

my_list.extend([6, 7, 8, 2, 5])  # Adding elements to the list
print(f"Extended list: {my_list}")

# Converting a list to a tuple
my_new_tuple = tuple(my_list)  # Converting list back to tuple      
print(f"Converted tuple: {my_new_tuple}")

count_2 = my_tuple.count(2)  # Counting occurrences of an element in the my_tuple
print(f"Count of 2 in my_tuple: {count_2}")

pos= my_tuple.index(2)  # Finding the index of an element in the tuple
print(f"Index of 2 in my_tuple: {pos}")

#unpacking a tuple
a, b, c, d, e = my_tuple  # Unpacking the tuple into variables
print("Unpacked values: ", a, b, c, d, e)

a, *b, c = my_tuple  # Unpacking with asterisk to collect remaining elements
print(f"Unpacked values with asterisk: {a}, {b}, {c}")  # a will be the first element, b will be a list of middle elements, c will be the last element

tuple1 = (1,2,3,4,5)
tuple2 = ('a', 'b', 'c', 'd', 'e')
combined_tuple = tuple1 + tuple2  # Concatenating two tuples
print(f"Combined tuple: {combined_tuple}")  # Output: (1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e')

# Repeating a tuple
repeated_tuple = tuple1 * 2  # Repeating the tuple
print(f"Repeated tuple: {repeated_tuple}")  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking if an element exists in a tuple
element_exists = 3 in my_tuple  # Checking if 3 is in the tuple
print(f"Does 3 exist in my_tuple? {element_exists}")  # Output: True

#List is mutable, tuple is immutable
#List is slower than tuple
#Tuple is faster than list and better performance

