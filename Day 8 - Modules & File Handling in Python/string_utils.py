# reversal of the String
def reverse(str):
    return str[::-1]

# palidrome check
def palidrome(str):
    strings = str[::-1]
    if str == strings:
        return "Given String is Palidrome"
    else:
        return "Given String is not a Palidrome"

# concatenation of two strings
def concatenation(str1, str2):
    return str1 + " " + str2 

# String Length
def length(str):
    return len(str)