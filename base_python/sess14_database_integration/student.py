# Python script to define a student class to map to the Student table in MySQL database

class Student:
    def __init__(self, student_no, name, birth_date, gender, city):
        """
        Represents a student in a learning institution.

        Attributes:
            student_no (str): The student's unique identifier.
            name (str): The student's name.
            birth_date (date): The student's date of birth.
            gender (str): The student's gender ('M' or 'F').
        """
        self.student_no = student_no
        self.name = name
        self.birth_date = birth_date
        self.gender = self._validate_gender(gender)
        self.city = city

    def _validate_gender(self, gender):
        """
           Validates the gender parameter to be either 'M' or 'F'.

            Args:
                gender (str): The gender value to validate.

            Raises:
                ValueError: If the gender is not 'M' or 'F'.

            Returns:
                str: The validated gender value.
        """
        if gender not in ['m', 'f']:
            raise ValueError("Invalid Gender!\nGender must be 'm' or 'f'")
        return gender

    # Method to return a string representation of the student object
    def __str__(self):
        """
         Returns a string representation of the student.

         Returns:
             str: A human-readable string containing the student's details.
        """
        gender_str = "Male" if self.gender == "m" else "Female"
        return (
            f"\n{'*'*50}"
            f"\nStudent: {self.name}\nStudent Number: {self.student_no}"
            f"\nDate Of Birth: {self.birth_date}\nGender: {gender_str}"
            f"\nCity Of Origin: {self.city}"
            f"\n{'*'*50}"
        )
