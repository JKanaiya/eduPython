"""
Python Dictionaries
This is a built in data type that represents a collection of key-value pairs, like a dictionary where
each word has a corresponding definition
Dictionaries are unordered, mutable, and can store elements of different types.
Each element in a dictionary is accessed by its key rather than its index
Dictionaries are created using {} curly braces.
Some dictionary operations are given below:
"""

# Student dictionary declaration
student = {"name": "MHD", "age": "20", "major": "Computer Science"}

# Display the length (number of keyv-value pairs) of the 'student' dictionary
print(f"Length of 'student' dictionary: {len(student)}")

# Fetch and display a view object (method to get the keys or values from a dictionary)
# of the keys in the 'student' dictionary
print(f"The keys from the 'student' dictionary are: {student.keys()}")

# Fetch and display a view object of the values in the 'student' dictionary
print(f"The values from the 'student' dictionary are: {student.values()}")

# Fetch and display a view object of the contents in the 'student' dictionary
print(f"The contents from the 'student' dictionary are: {student.items()}")

# Get and display a value using its key from the 'student' dictionary
print(f"Displaying the students name: {student.get('name')}")
print(f"Displaying the students name: {student['name']}")

# Remove and display the contents of a iven key when it exists in the 'student' dictionary
# else return / give back and optional default value
phone_no = student.pop("phone_no", "Phone number was not provided during registration")
print(f"The value of 'phone_no' is {phone_no}")

# Remove and display the contents of the last key-value pair in the 'student' dictionary
print(f"The last key-value pair in the 'student' dictionary is: {student.popitem()}")

# Update and display the contents of the 'student' dictionary
student.update({"age": 21, "grade": "A", "phone_no": "0712345678"})
print(f"The updated contents of the 'student' dictionary are: {student.items()}")

# Create a copy of the "student" dictionary
copy_of_student = student.copy()
print(f"The contents of 'copy_of_student' dictionary are: {copy_of_student}")

# Fetch and return the value associated with a given key when not found assign it with a default value
major = student.pop("major", "Not defined")
print(f"The value of 'major' in the 'student' dictionary is: {major}")

# Create and display a new dictionary for the keys of an existing dictionary
new_dict = dict.fromkeys(student.keys())
print(f"The contents of 'new_dict' dictionary are: {new_dict}")

# Delete a specific key-value pair from the 'student' dictionary
# and display the remaining key-value pairs
del student["grade"]
print(f"The contents of 'new_dict' dictionary after removing 'grade' are: {student}")

# Find out and display whether a given key exists in the dictionary
print(f"Does 'age' exist in the 'student' dictionary?: {'age' in student}")
print(f"Does 'grade' exist in the 'student' dictionary?: {'grade' in student}")

# Remove all the content from the stuedn dictionary and display
student.clear()
print(f"After clearing 'student' dictionary we get: {student}")
