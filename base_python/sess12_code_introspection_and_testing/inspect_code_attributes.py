# Python script to demonstrate using introspection to display object attributes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"Hello there, my name is {self.name}, and I'm {self.age} years old")

# Create an instance of the person
p1 = Person("MHD", 20)
if isinstance(p1, Person):
    print(f"{p1.name} is an instance of the 'Person' class and is {p1.age} years old")
else:
    print(f"The 'p1' variable is an instance of {type(p1)}")

# Use the dir() method to lsit the attributes and method of the 'p1' object
print(f"Attributes and methods of the 'p1' object are:\n {dir(p1)}")
