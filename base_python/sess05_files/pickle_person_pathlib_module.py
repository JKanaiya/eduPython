# Python script to get a person's details from the user and store them in
# the 'person_pathlib.txt' file in the files folder / directory
# This verison uses the pathlib module in the standard Python library which is more
# portable and works across different Operating systems without the need to manually
# handle file seperators or abosilute paths

# Import the required modules
import pickle
from pathlib import Path
from person import Person

# Prompt the user for their names and age
name = input('Enter your name: ')
age = int(input('Enter your age: '))

# Create a Person object
person1 = Person(name, age)

# Get the path to the file to be created
# file_path = os.path.abspath(os.path.join(os.getcwd(), "..", "person_os.txt"))
file_path = Path.cwd().parent / "files" / "person_pathlib.txt"

# Ensure the directory exists if not create it
file_path.parent.mkdir(parents=True, exist_ok=True)

# Pickle the Person object
with open(file_path, "wb") as f:
    pickle.dump(person1, f)

# Notify the user about successfully pickling their details
print(f"The 'person1' object has been successfully pcikled in {file_path}")