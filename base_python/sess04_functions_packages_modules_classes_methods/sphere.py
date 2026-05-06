# Python file to define a Sphere class

# Import the required module(s)
from circle import Circle


class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def calc_volume(self):
        return 4.0 / 3.0 * self.calc_area() * self.radius

    def calc_surface_area(self):
        return 4 * self.self.calc_area()

    def __str__(self):  # dunder method works like to string
        """
        Returns a formatted string representing the sphere's dimensions.

        Returns:
            str: a formatted string representing the sphere's dimensions (surface area, Volume, Radius)'
        """
        return (f"sphere dimensions:\n"
                f"Radius: {self.radius}"
                f"Surface Area: {self.calc_area():.2f}cm^2"
                f"Volume: {self.calc_perimeter():.2f}cm^3")
