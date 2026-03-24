# Python script that uses closures to serialize and deserialize
# a student object to and from a JSON file

import json
import os
from datetime import datetime, date


# -------------------------------
# Student class
# -------------------------------
class Student:
    """
    A class to represent a student.
    """

    def __init__(self, reg_no, name, birthdate, gender):
        self.reg_no = reg_no
        self.name = name
        self.birthdate = birthdate  # datetime.date
        self.gender = gender

    def to_dict(self):
        """Convert Student object to a JSON-serializable dictionary."""
        return {
            "reg_no": self.reg_no,
            "name": self.name,
            "birthdate": self.birthdate.isoformat(),  # FIX: date → string
            "gender": self.gender,
        }

    @staticmethod
    def from_dict(data):
        """Create a Student object from a dictionary."""
        return Student(
            reg_no=data["reg_no"],
            name=data["name"],
            birthdate=datetime.strptime(
                data["birthdate"], "%Y-%m-%d"
            ).date(),  # FIX: datetime → date
            gender=data["gender"],
        )


# -------------------------------
# Closures for JSON handling
# -------------------------------
def student_json_handler(file_path):
    """
    Returns two closure functions:
    - serialise(student)
    - deserialise()
    """

    def serialise(student):
        with open(file_path, "w") as f:
            json.dump(student.to_dict(), f, indent=4)
        print(f"Student serialized successfully to: {file_path}")

    def deserialise():
        with open(file_path, "r") as f:
            data = json.load(f)
        student = Student.from_dict(data)
        print(f"Student deserialized successfully from: {file_path}")
        return student

    return serialise, deserialise


# -------------------------------
# Run the application
# -------------------------------
if __name__ == "__main__":
    # Create a Student object
    student = Student("EICN-1234", "Muhammad Hasan", date(2006, 3, 25), "Male")

    # Build file path
    file_path = os.path.abspath(
        os.path.join(os.getcwd(), "..", "files", "students.json")
    )

    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Get closure functions
    serialize, deserialize = student_json_handler(file_path)

    # Save student to JSON
    serialize(student)

    # Load student from JSON
    loaded_student = deserialize()

    # Display loaded student details
    print(f"\nLoaded student details:")
    print(f"Name: {loaded_student.name}")
    print(f"Reg No: {loaded_student.reg_no}")
    print(f"Birthdate: {loaded_student.birthdate}")
    print(f"Gender: {loaded_student.gender}")
