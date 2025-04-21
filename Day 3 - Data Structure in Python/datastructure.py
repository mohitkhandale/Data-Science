#List -> Orderedd Collection of items
#Tuple -> Ordered Collection of items, immutable
#Set -> Unordered Collection of items, no duplicates
#Dictionary -> Unordered Collection of key-value pairs

#List
# List is a collection of items that are ordered and changeable. It allows duplicate members.
# Lists are defined by having values between square brackets [ ].
mylist1 = [] # empty list
mylist2 = ["apple", "banana", "cherry"] # list with items
mylist3 = ["apple", "banana", "cherry", 1, 2, 3, True] # list with different data types

#type() function returns the type of an object
print(type(mylist1)) # <class 'list'>

#Nested Lists
mylist4 = ['One',[1,2,3],[4,5,6]] # list with nested lists
print(mylist4) # ['One', [1, 2, 3], [4, 5, 6]]

print(mylist4[1]) # [1, 2, 3] # access the second item in the list
print(mylist4[1][1]) # 1 # access the first item in the second list
print(mylist4[2][2]) # 6 # access the third item in the third list

#slicing
letters = ['a', 'b', 'c', 'd', 'e'] # list with letters
print(letters[-3:-1])# ['c', 'd'] # access the third to first item in the list

#max(), min() and sum() functions
mylist5 = [10, 25, 5, 60, 15, True, False] 
min_value = min(mylist5) # False # returns the minimum value in the list
max_value = max(mylist5) # 60 # returns the maximum value in the list
sum_value = sum(mylist5) # 110 # returns the sum of the values in the list
print(min_value, max_value) # False 60
print(sum_value) # 110

strings = ['apple', 'banana', 'cherry'] # list with strings
print(min(strings)) # apple # returns the minimum value in the list
print(max(strings)) # cherry # returns the maximum value in the list
#String is compared based on the ASCII value of the characters in the string.
#The ASCII value of 'a' is 97, 'b' is 98 and 'c' is 99. So, the minimum value in the list is 'apple' and maximum value is 'cherry'

#why the list is mutable?
mylist6 = [1, 2, 3, 4, 5] # list with numbers
mylist6[3] = 10 # change the value of the fourth item in the list
print(mylist6) # [1, 2, 3, 10, 5] # change the value of the fourth item in the list
print(mylist6 * 3) # [1, 2, 3, 10, 5, 1, 2, 3, 10, 5, 1, 2, 3, 10, 5] # repeat the list three times

#inbuild functions of list
mylist7 = [1, 2, 3, 4, 5] # list with numbers
mylist7.append(6) # add an item to the end of the list
mylist7.insert(0, 0) # add an item to the beginning of the list
mylist7.remove(3) # remove an item from the list
mylist7.pop() # remove the last item from the list
mylist7.sort() # sort the list in ascending order
mylist7.reverse() # reverse the list
mylist7.clear() # remove all items from the list
mylist7.extend([7, 8, 9]) # add multiple items to the end of the list
mylist7.copy() # create a copy of the list
mylist7.count(1) # count the number of times an item appears in the list
mylist7.index(1) # return the index of the first occurrence of an item in the list
mylist7.index(1, 0, 3) # return the index of the first occurrence of an item in the list between the specified range
mylist7.sort(reverse=True) # sort the list in descending order
mylist7.sort(key=str) # sort the list in ascending order based on the string value of the items in the list
mylist7.sort(key=str, reverse=True) # sort the list in descending order based on the string value of the items in the list
mylist7.sort(key=len) # sort the list in ascending order based on the length of the items in the list
mylist7.sort(key=len, reverse=True) # sort the list in descending order based on the length of the items in the list


