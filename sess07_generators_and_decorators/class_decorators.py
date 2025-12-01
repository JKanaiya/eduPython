# Python script to demonstrate decorating a class (using a loger function)

# Define the logger function
def log_dimensions(cls):
    def wrapper(*args, **kwargs):
        print(f"Logging dimensions of {cls}")
        rectangle = cls(*args, **kwargs)
        print(f"Rectangle dimensions logged!")
        return rectangle

    return wrapper


@log_dimensions
class Rectangle:
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

    def __str__(self):
        return (
            f"Rectangle's Dimensions"
            f"\nWidth: {self.width} cm"
            f"\nLength: {self.length} cm"
            f"\nArea: {self.calculate_area()} cm²"
            f"\nPerimeter: {self.calculate_perimeter()} cm"
        )


# Prompt the user for the dimensions of a new reactangle
length = int(input("Enter the length of the rectangle in cm: "))
width = int(input("Enter the width of the rectangle in cm: "))

# Create / instantiate a Rectangle obejct with the above dimensions
rectangle = Rectangle(width, length)
print(rectangle)

# Creae / instantiate a Rectangle object with hard-coded values
rectangle2 = Rectangle(8, 5)
print(rectangle2)
