# Given a string and the task is to count vowels, consonant and special character in string. Store input string in variable sentence.Special character also contains the white space and digits.

# Input Format

# welcome to sipna

# Constraints

# sentense > 0

# Output Format

# Vowels: 6
# Consonant: 8
# Special Character: 2

sentence = input()
vowels = 0
consonant = 0
special_character = 0

for i in sentence:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vowels += 1
        else:
            consonant += 1
    else:
        special_character += 1

print(f"Vowels: {vowels}\nConsonant: {consonant}\nSpecial Character: {special_character}")