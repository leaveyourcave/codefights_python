# 1
def add(param1, param2):
    "We have to add two numbers."
    return param1 + param2

# 2
def centuryFromYear(year):
    "We have to calculate the century for a given year."
    return (year - 1) / 100 + 1

# 3
def checkPalindrome(inputString):
    "Determine whether given string is a palindrome."
    return inputString == inputString[::-1]
