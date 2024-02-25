# For any given number n where n is a natural number, For input 0 pattern will be disappear.And in exception case this will print NA, print number increasing pattern. n = 4

# 1 1 2 1 2 3 1 2 3 4

# Input Format

# n = 4

# Constraints

# n > 0

# Output Format

# 1
# 1 2
# 1 2 3
# 1 2 3 4

n = int(input())
if n == 0:
    print("")
elif n < 0:
    print("NA")
else:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()