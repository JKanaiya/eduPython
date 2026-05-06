# Python script to demonstrate assignment statements

# Basic assignment
num1 = 5
spam = "Yum"
print(f"The contents of 'num1': {num1}")
print(f"The contents of 'spam': {spam}")

# Tuple assignment (positional)
spam, ham = "Spam", "YUM"
print(f"The contents of 'spam' and 'ham' after tuple assignment are: {spam} and {ham}")

# List assignment (positional)
[car, drink] = ["CX-5", "juice"]
print(f"The contents of car and drink after tuple assignment: {car}, and {drink}")

# Sequence assignment for numeric values (used on iterables & strings)
first_num, second_num, third_num, fourth_num = [5, 8, 4, 7]
print(f"The contents of 'first_num': {first_num}"
      f"\nThe contents of 'second_num': {second_num}"
      f"\nThe contents of 'third_num': {third_num}"
      f"\nThe contents of 'fourth_num': {fourth_num}")

# Sequence assignment for alphanumeric values ()
first_char, second_char, third_char, fourth_char = "Cx-5"
print(f"The contents of 'first_char': {first_char}"
      f"\nThe contents of 'second_char': {second_char}"
      f"\nThe contents of 'third_char': {third_char}"
      f"\nThe contents of 'fourth_char': {fourth_char}")

# Sequence assignment for numeric values (used on iterables & strings)
first_num, second_num, *other_num, eighth_num = [5, 8, 4, 7, 12, 3, 1, 12]
print(f"The contents of 'first_num': {first_num}"
      f"\nThe contents of 'second_num': {second_num}"
      f"\nThe contents of '*other_num': {other_num}"
      f"\nThe contents of 'eighth_num': {eighth_num}")

# Sequence assignment for alphanumeric values ()
first_char, second_char, *other_char, eighth_char = "CHICKENS"
print(f"The contents of 'first_char': {first_char}"
      f"\nThe contents of 'second_char': {second_char}"
      f"\nThe contents of 'third_char': {other_char}"
      f"\nThe contents of 'fourth_char': {fourth_char}")

# Multiple target assignment
print(f"The contents of 'first_num' 'second_num' and 'third_num'"
      f" before multiple assignment are: {first_num}, {second_num}, {third_num}")

first_num = second_num = third_num = 8
print(f"The contents of 'first_num' 'second_num' and 'third_num'"
      f" after multiple assignment are: {first_num}, {second_num}, {third_num}")

# Augmented assgnment (shorthand assignment in C-based languages)
second_num += 2 # same as second_num = second_num + 2
print(f"After incrementing / adding 'second_num': {second_num}")