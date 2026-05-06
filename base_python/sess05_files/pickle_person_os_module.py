# Python script to get a person's details from the user and store them in
# the 'person_os.txt' file in the files folder / directory

# Import the required modules
import pickle
import os
from person import Person

# Prompt the user for their names and age
name = input('Enter your name: ')
age = int(input('Enter your age: '))

# Create a Person object
person1 = Person(name, age)

# Get the path to the file to be created
file_path = os.path.abspath(os.path.join(os.getcwd(), "..", "person_os.txt"))

# Display the path to the file to be created pr appended to
print(f"File paht: {file_path}")

# Pickle the Person object
with open(file_path, "wb") as f:
    pickle.dump(person1, f)

# Notify the user about successfully pickling their details
print(f"The 'person1' object has been successfully pcikled in {file_path}")