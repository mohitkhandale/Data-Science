# Sets is a collection of unordered, unindexed, and unique elements.
# Sets are mutable, meaning you can add or remove elements after creation.
# Sets are defined using curly braces {} or the set() constructor.
# Duplicate elements are automatically removed in a set and not allowed.
# Sets are useful for membership testing, removing duplicates from a collection, and performing mathematical set operations like union, intersection, and difference.


set1 = set() #Empty Set
set2 = {1, 2, 3, 4, 5}  # Set with initial elements
set3 = {1, 2, 3, 4, 5, 1, 2}  # Duplicate elements are removed
set4 = {1, 2, 3, 4, 5, 'a', 'b', 'c'}  # Mixed data types are allowed

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Set3: {set3}")
print(f"Set4: {set4}")

# Accessing elements in a set is not possible like lists or tuples, as sets are unordered.
# However, you can check for membership using the 'in' keyword. 
print(f"Is 3 in set2? {'Yes' if 3 in set2 else 'No'}")

# Adding elements to a set
set2.add(6)  # Adding a single element
print(f"Set2 after adding 6: {set2}")

# Adding multiple elements to a set
set2.update([7, 8, 9])  # Adding multiple elements
print(f"Set2 after adding multiple elements: {set2}")

# Removing elements from a set
set2.remove(2)  # Removing an element (raises KeyError if not found)
print(f"Set2 after removing 2: {set2}")

# Discarding an element (does not raise an error if not found)
set2.discard(10)  # Discarding an element (does not raise an error if not found)
print(f"Set2 after discarding 10: {set2}")

len(set2)  # Getting the number of elements in the set
print(f"Number of elements in set2: {len(set2)}")   

min_element = min(set2)  # Finding the minimum element in the set
max_element = max(set2)  # Finding the maximum element in the set
print(f"Minimum element in set2: {min_element}")
print(f"Maximum element in set2: {max_element}")

sum_elements = sum(set2)  # Finding the sum of all elements in the set
print(f"Sum of elements in set2: {sum_elements}")

# Converting a set to a list
my_list = list(set2)  # Converting set to list
print(f"Converted list from set2: {my_list}")

# Converting a list to a set
my_set = set(my_list)  # Converting list back to set
print(f"Converted set from list: {my_set}")

 # Join Sets
set5 = {10, 20, 30}
set6 = {20, 30, 40, 50}
union_set = set5.union(set6)  # Union of two sets
print(f"Union of set5 and set6: {union_set}")

intersection_set = set5.intersection(set6)  # Intersection of two sets
print(f"Intersection of set5 and set6: {intersection_set}")
# set5 & set6  # Another way to find intersection using '&' operator

difference_set = set5.difference(set6)  # Difference of two sets
print(f"Difference of set5 and set6: {difference_set}")
# set5 - set6  # Another way to find difference using '-' operator

symmetric_difference_set = set5.symmetric_difference(set6)  # Symmetric difference of two sets
print(f"Symmetric difference of set5 and set6: {symmetric_difference_set}")
# set5 ^ set6  # Another way to find symmetric difference using '^' operator

#Exercise: Merge the below to tuple and then removee the duplicate values and return the final output as a tuple
tup1=(1,2,3)
tup2=(3,4,5)
merged_tuple = tup1 + tup2
mysets = set(merged_tuple)
tuple_op = tuple(mysets)
print(f"Result after merging and removing duplicates: {tuple_op}")

#another way to merge two tuples and remove duplicates using function definition
def merge_and_remove_duplicates(tup1, tup2):
   return tuple(set(tup1).union(set(tup2)))

print(f"Result after merging and removing duplicates using function: {merge_and_remove_duplicates(tup1, tup2)}")

