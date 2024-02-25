# For any given number n,For input 0 pattern will be disappear.And in exception case this will print NA, print solid Squares made with stars(*).

# Input Format

# n = 4

# Constraints

# n > 0

# Output Format

# ****
# ****
# ****
# ****

n = int(input())
if n == 0:
    print("")
elif n < 0:
    print("NA")
else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*", end="")
        print()
        