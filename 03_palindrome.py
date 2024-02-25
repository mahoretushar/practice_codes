# Given a positive integer,Let x be the given integer. write a function that returns true if the given number is a palindrome, else false.For invalid input print NA. For example, 12321 is a palindrome, but 1451 is not a palindrome.

# Input Format

# 12321
# 1451
# Constraints

# x >= 0

# Output Format

# Yes
# No

x = int(input())
temp = x
sum = 0

def is_palindrome(x):
    if x < 0:
        return "NA"
    temp = x
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum * 10 + digit
        temp //= 10
    if x == sum:
        return "Yes"
    else:
        return "No"