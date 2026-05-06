# Python script to unpickle the person's details from the 'person_os.txt' file and display them

# Import the required modules
import pickle, os

# Variables to hold the path to the 'person_os.txt'
file_path = os.path.abspath(os.path.join(os.getcwd(), "..", "person_os.txt"))

# List that will hold the Person objects orm the 'person_os.txt'
persons = []

# Open the 'person_os.txt' file and read its contents
with open(file_path, "rb") as f:
    while True:
        try:
            unpickled_person = pickle.load(f)
            persons.append(unpickled_person)
        except EOFError:
            break # End of file reached

# Access and display the unpickled persons attributes
if persons:
    print(f"Detail of the persons in the 'person_os.txt' file:")
    for index, person in enumerate(persons, start=1):
        print(f"Person {index}. Name: {person.name} Age: {person.age}")