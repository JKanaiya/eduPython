# Python script to demonstrate simple comprehension operations on a set dictionary

# Import the required modules
names = ["Sam", "Paul", "Nemo", "j", "memo"]
print(f"List of names and initial: {names}")

# Obtain a set of unique names that have more than one character using a set comprehensions
names_set = {name[0].upper() + name[1:].lower() for name in names if len(name) > 1}

# Display the unique set of names
print(f"List of unique names set: {names_set}")

# Dictionary of the occurances of different letters in the lower and uppercase forms
test_dic = {"l": 10, "b": 34, "Z": 2, "N": 4, "L": 4, "z": 5}

# Display the dictionary in its original form
print(f"Original dictonary: {test_dic}")

# Get and display the total occurance of each letter regardless of case using a dictionary
letter_count = {
    k.lower(): test_dic.get(k.lower(), 0) + test_dic.get(k.upper(), 0)
    for k in test_dic.keys()
}

print(f"The total count for eahc letter irregardless of case is: {letter_count}")
