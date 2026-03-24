"""
Python Lists
A Python List is a built in data type that represents an ordered collection of items / elements,
that are homogeneous in nature.
Lists allow duplicates and are mutable (i.e their elements can be modified, added or removed)
Lists are created using [] or list() constructor
A sample list and some of its operations are given below
"""

# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Display the fruits in the fuits list
print(f"The initial fruits in the list are: {fruits}")

# Display the number of items / elements in the fruit list
print(f"The number of fruits in the fruit list is: {len(fruits)}")

# Add a fruit to the end of the fruit list
fruits.append("orange")
print(f"After adding 'orange' to the fruit list, the new list is: {fruits}")

# Add the contents of another list of fruits to our fruit list
fruits.extend(["mango", "grapes", "kiwi", "pineapple", "strawberry"])

# Display the combined list of fruits
print(f"The complete list of fruits is {fruits}")

# Insert a fruit (item / element) at a given / specified index
fruits.insert(1, "pears")
print(f"After inserting 'pears' to the fruit list, the new list is: {fruits}")

# Remove a fruit (item / element) at a given/specified index
removed_fruits = fruits.pop(3)
print(f"The removed fruit is: {removed_fruits}")
print(f"After removing {removed_fruits} from the fruit list, the new list is: {fruits}")

# Remove a specific fruit(item / element) from the list
fruits.remove("banana")
print(f"After removing 'banana' from the fruit list, the new list is: {fruits}")

# Get and display the index of an item / element in the list
print(f"The first occuarnace of 'mango' is: {fruits.index('mango')}")

# Get and displa the occurance(s) of a given item / element in the list
print(f"'apple' occurs: {fruits.index('apple')} time(s) in the fruits list")

# Sort and display the fruits list in alphabetical order
fruits.sort()
print(f"After sorting the fruits list: {fruits}")

# Sort and display the fruits list in reverse alphabetical order
fruits.reverse()
print(f"After reversing the fruits list: {fruits}")

# Get and display the minimum and maximum items / elements in the list
# (least and highest fruits letterwise)
print(
    f"The least fruit letterwise is: {min(fruits)}\n The highest fruit letterwise is {max(fruits)}"
)

# Creating a copy of the fruits list
copy_of_fruits = fruits.copy()
print(f"The copied fruits list is: \n{copy_of_fruits}")

# Clearing the fruits list
fruits.clear()
print(f"After removing all fruits we get: {fruits}")

# Re-assigning the frsuits list
fruits = [
    "apple",
    "kiwi",
    "grape",
    "orange",
    "tangerine",
    "lemon",
    "avacado",
    "cocnut",
    "fig",
]

print("*" * 40)
# Displaying the new fruits list
print(f"After re-assignment, the new fruits list is: {fruits}")

# Displaying the first 3 fruits in the fruits list
print(f"The frist 3 fruits in the fruits list are: {fruits[:3]}")

# Display the last 2 fruits in the list
print(f"The last 2 items in the fruits list are: {fruits[-2:]}")

# Display every second fruits starting from the second one
print(f"Starting from the second fruit and skipping one fruit we get: {fruits[1::2]}")

# TODO: Dislay every 3rd fruit in the fruit list
print(f"Every 3rd fruit in the fruits list is: {fruits[2::3]}")

# DIsplay all the fruits apart from the first one and the last one
print(f"ALl fruits except 1st and last one: {fruits[1:-1]}")

# Display all the fruits in reverse order starting from the 3rd last fruit
print(f"All fruits starting from 3rd last: {fruits[-3::-1]}")

# Get and display an empty slice from the fruit list
print(f"The empty slice from the fruit list is: {fruits[len(fruits) - 1 : 3]}")
