# Python file to define a Circle class

# Import the required modules
import math  # Allows us to access the inbuilt value of PI and pow() function


class Circle:
    """
    A class to represent a gemoetric circle.

    Attributes:
        radius (float): the radius of the circle in cm.

    Methods:
        calc_area(): calculates and returns the area of the circle.
        calc_perimeter(): calculates and returns the perimeter of the circle.
        __str__(): returns a formatted string representing the circle's dimensions.
    """

    def __init__(self, radius=0):
        """
        Initialise the circle with a given radius

        Parameters:
            radius (float), default 0: the radius of the circle in cm.
        """
        self.radius = radius

    def calc_area(self):
        """
        Calculates the area of the circle (π * r²).

        Returns:
            float: the area of the circle.
        """
        return math.pi * pow(self.radius, 2)

    def calc_perimeter(self):
        """
        Calculates the perimeter of the circle, π * (2 * r).

        Returns:
            float: the perimeter of the circle.
        """
        return math.pi * (2 * self.radius)

    def __str__(self):  # dunder method works like to string
        """
        Returns a formatted string representing the circle's dimensions.

        Returns:
            str: a formatted string representing the circle's dimensions (area, circumference, area)'
        """
        return (f"Circles dimensions:\n"
                f"Radius: {self.radius}"
                f"Area: {self.calc_area():.2f}cm^2"
                f"Perimeter: {self.calc_perimeter():.2f}cm")


# print(f"The documentation string of calc_area() method is:\n{Circle.calc_area.__doc__} ")
