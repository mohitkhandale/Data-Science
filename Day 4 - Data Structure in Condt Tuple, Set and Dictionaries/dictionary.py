# Dictionary in python is a unordered collection of items.
# It is mutable and indexed by keys.
# Dictionary is defined by curly braces {} and key-value pairs.
# Dictionary is in key:value format.
# Dictionary, we can also understand as custiomized data structure.
# Dictionary is a hash table implementation in Python.
# Dictionary uses Hashing Data Structure

my_dict={"name":"John", "age":30, "city":"New York"}
print(my_dict)
print(type(my_dict))
print(my_dict["age"]) # Accessing value using key

#Built-in functions
print(my_dict.keys())  # Returns a view object that displays a list of all the keys in the dictionary
print(my_dict.values())  # Returns a view object that displays a list of all the values in the dictionary
print(my_dict.items())  # Returns a view object that displays a list of dictionary's key-value tuple pairs
print(min(my_dict))  # Returns the smallest key in the dictionary
print(max(my_dict))  # Returns the largest key in the dictionary
print(len(my_dict))  # Returns the number of items in the dictionary

# In Python, dictionary is mutable, we can add, remove and change items in the dictionary.
# But we cannot change the key of the dictionary. Keys Are Immutable.

my_dict['position'] = 'Software Engineer'  # Adding a new key-value pair
my_dict['company'] = 'Tech Corp'  # Adding another key-value pair
print(my_dict)

my_dict.update({'salary': 50000})  # Updating the dictionary with another dictionary
print(my_dict)

del my_dict['age']  # Deleting a key-value pair
print(my_dict)

my_dict.pop('city')  # Removing a key-value pair using pop method
print(my_dict)

# Excercise 1: Check if a key exists in the dictionary
list1 = ['name', 'age', 'city', 'position', 'company', 'salary']
def all_unique(list1):
    return len(list1) == len(set(list1))
print(all_unique(list1))  # Check if all keys are unique

