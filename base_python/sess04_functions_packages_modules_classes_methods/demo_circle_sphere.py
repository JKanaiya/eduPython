# Python file to demonstrate working with user-defined / custom class and instantiating them

# Import the required modules
from circle import Circle
from sphere import Sphere

# Prompt the user for the cricle's radius
radius = float(input("Enter the radius of the circle in centimeters: "))

# Creat or instantiate circle object
circle1 = Circle(radius)
sphere1 = Sphere(radius)

print(circle1)
print(sphere1)
