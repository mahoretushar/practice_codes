# Given a number x, determine whether the given number is Armstrong’s number or not.

# A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if

# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

# Input Format

# 153

# Constraints

# x>=0

# Output Format

# Yes
# 153 is an Armstrong number.

x = int(input())
temp = x
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if x == sum:
    print(f"Yes\n{x} is an Armstrong number.")
else:
    print(f"{x} is not an Armstrong number.")