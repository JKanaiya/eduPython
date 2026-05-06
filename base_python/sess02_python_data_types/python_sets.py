"""
Python sets
A set in python is a built in type that represents an unordered collection of elements of the same or different types
Sets DONT allow duplicates and are mutable. Theyare suitable fro tasks that involve checking membership, removing
duplicates and perfroming mathematical operations like intersection, uniion, difference and symmetric_difference

Sets are created  using the curcly braces {} or set() constructor
"""

# Create a set of fruits
fruits = {"apple", "banana", "cherry", "durian", "orange", "elephant apple"}

# Dispaly the contents of the fruit set
print(f"The fruit in the fruits set are: {fruits}")

# Display the number of fruits in the fruits set
print(f"The number of fruits in the set are: {len(fruits)}")

# Add 'orange' to the fruits set
fruits.add("orange")
print(f"After adding 'orange' to the frui set we get: {fruits}")

# Remove 'banana' from the fruit
fruits.remove("banana")
print(f"After removing 'banana' from the set we get: {fruits}")

# Discard 'cherry' from the fruit set
fruits.discard("cherry")
print(f"After discarding 'cherry' from the set we get: {fruits}")

# Remove the last item from the set
popped_fruit = fruits.pop()
print(f"After poppping fruits we get: {fruits}")

# Copy the set of remaining fruits to a new set and display them
copy_of_fruits = fruits.copy()
print(f"After copying the remaining fruits to a new set we get {copy_of_fruits}")

# Declare another set of fruits
more_fruits = {"pear", "avocado", "mango", "pineapple"}

# Create a new combined set of fruits and display it
combined_fruits = fruits.union(more_fruits)
print(f"The combined set of fruits is : {combined_fruits}")

# Get and display the common fruits in the 'combined_fruits' and 'more_fruits' set
common_fruits = combined_fruits.intersection(more_fruits)
print(f"The common set of fruits is : {common_fruits}")


# Get and display the fruits that are in 'fruits' set but not in  'more_fruit'
fruits_difference = fruits.difference(more_fruits)
print(f"The difference of fruits we get is : {fruits_difference}")

# Get and display the fruits that are either in 'fruits' or in 'more_fruits' but not in both
symmetric_fruits = fruits.symmetric_difference(more_fruits)
print(f"The symmetric set of fruits we get is : {fruits ^ more_fruits}")
print(f"The symmetric set of fruits we get is : {symmetric_fruits}")

# Check and display whether fruit set is a subset of "more_fruits"
print(f"'fruit' set is a superset of 'more_fruits': {fruits.issuperset(more_fruits)}")

# Check and display wether 'fruit' set and 'more_fruit' set have no common fruit elements
is_disjoint_fruits = fruits.isdisjoint(more_fruits)
print(
    f"'fruit' set and 'more_fruits' set have no common fruit / elements: {is_disjoint_fruits}"
)

# Create another fruit set and use it to update the set of fruits: CAUTION...overwrites set elements
other_fruits = {"watermelon", "strawberry", "blueberry"}
fruits.update(other_fruits)
print(f"After updating the 'fruits' set we get: {fruits}")

print(f"Here: {fruits <= fruits.copy()}")

# Clear and display the 'fruits' set
fruits.clear()
print(f"After clearing the 'fruits' set we get: {fruits}")

