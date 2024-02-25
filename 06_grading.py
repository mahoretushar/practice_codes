# I have an assignment for school and one of the tasks is to display the grades that the students will be receiving.Let marks be the input given.This is the grading system for one subject.Student can achieve at maximum 100% and negative marking is not allowed. The grades are:

# A: 90% +
# B: 80% - 89%
# C: 70% - 79%
# D: 60% - 69%
# E: 50% - 59%
# F: Below 49
# Input Format

# 95
# 69
# 33
# Constraints

# 101< marks >= 0

# Output Format

# A
# D
# F

marks = int(input())
if marks > 100 or marks < 0:
    print("Invalid input")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 50:
    print("E")
else:
    print("F")
