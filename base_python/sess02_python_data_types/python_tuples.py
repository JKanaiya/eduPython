"""
Python Tuples
A tuple is a built in data type that represents an ordered collection of elements of the same type.
Tuples allow duplicates and are immutable (their elements cannot be modified0
Tuples are created using () rounded brackets / parnethesis
Tuples are generally fater than lists as python doesnt have to wory about growing or shrinking them.
Some tuple operations are given below
"""

# Create a tuple of fruits
fruits = ("blueberry", "orange", "apple", "banana", "cherry", "avocado", "guava", "blueberry")

# Display the fruits in the tuple and their number
print(f"The fruits in the tuple are: {fruits}.\nThe number of fruits in the tuple is {len(fruits)}")

# Get and display the index of an item/element in the tuple
print(f"The index of 'avocado' is {fruits.index('avocado')}")

# Get and display the number of occurances of blueberry in the tuple
print(f"Blueberry appears {fruits.count('blueberry')} times in the tuple")

# Combine two tuples to create a third one and display its contents
combined_fruits = fruits + ("kiwi", "watermelon", "pineapple", "dragon fruit")
print(f"The combined fruits are: {combined_fruits}.")

# Create a tuple that repeats the tuple twice
fruits_repeated = fruits * 2
print(f"The repeated fruits list is: {fruits_repeated}")

# Create a sorted tuple of fruits
sorted_fruits = sorted(fruits)
print(f"The sorted fruits tuple: {sorted_fruits}")

# Display the minimum and maximum fruit in the tuple
print(f"The maximum fruit in the tuple is: {max(fruits)}\nThe minimum fruit in the tuple is {min(fruits)}")

# Declare a tuple of number
numbers = (1, 2, 3, 4)

# Display the tuple of numbers and its sum
print(f"The 'numbers' tuple contains: {numbers} and their sum is {sum(numbers)}")

# Display the first 3 numbers in the tuples
print(f"The first 3 numbers in the tuple are: {numbers[:3]}") # Same as {numbers[0:3]}

# Display only the odd numbers from the 'numbers' tuple
print(f"Odd numbers from the tuple: {numbers[::2]}") # same as {numbers[0::2]}

# use the 'any()' function to check if any element in the 'numbers' tuple is true
# In python, non-zero numbers are considered true, since all numbers in the tuple are non-zero,
# in 'any(numbers)' will return True
any_true = any(numbers)
print(f"'any_true' tuple contains: {any_true}")

# use the 'all()' function to check if all elements in the 'numbers' tuple are true
# Since all elements (1, 2, 3, 4) are non-zero, they are all considered true and will return True
all_true = all(numbers)
print(f"'all_true' tuple contains: {all_true}")