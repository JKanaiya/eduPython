# Python script to demonstrate Python's number / numeric types
# Get the code to make Decimal numbers work
from decimal import Decimal, getcontext, ROUND_DOWN

# Get the code to make Fraction numbers work
from fractions import Fraction

# Demonstrate integers (whole numbers, both positive and negative)
int_value = 8
print("Integer Demonstration")
print("*" * 40)
print(f"The value of int_value is {int_value}")
print(f"The type of int_value is: {type(int_value)}\n")


# Demonstrate floating point numbers (numbers with fractional components, both negative and positive)
float_value = 3.3333333333333
print("Floating-point Number Demonstration")
print("*" * 40)
print(f"The value of float_value is {float_value}")
print("The value of float_value correct to 4 d.p is %.4f" % float_value)
print(f"The type of float_value is: {type(float_value)}\n")

# Demonstrrate Decimal (with decimal places and a fixed precision, both negative and positive)
# Set the precision for decimal operations
getcontext().prec = 7  # Set a higher precision when you need to maintain accuracy
# For rounding numbers with lots of decimal places e.g Decimal('345.23456789')

decimal_value = Decimal(8.14159238)
print("Decimal Number Demonstration")
print("*" * 40)
print(f"The original value of 'decimal_value' is {decimal_value}")
# Using ROUND_DOWN to ensure no rounding up takes place
decimal_value = Decimal(1.23456789012345678).quantize(
    Decimal("0.1234"), rounding=ROUND_DOWN
)
print(f"The rounded value of 'decimal_value' correct to 4 d.p is {decimal_value}")

# Demonstrate Complex Numbers
complex_value = 3 + 4j
print("Complex Number Demonstration")
print("*" * 40)
print(f"The original value of 'complex_value' is {complex_value}")
print(f"The real part of the value of 'complex_value' is {complex_value.real}")

# Demonstrate Fraction (rational numbers)
fraction_value = Fraction(7, 3)
print("Fraction Number Demonstration")
print("*" * 40)
print(f"The value of 'fraction_value' is: {fraction_value}")
print(f"The type of 'fraction_value' is: {type(fraction_value)}\n")

# Demonstrating Boolean (True or False)
true_value = True
false_value = False
n = 5
a = 8
print("Boolean Value Demonstration")
print("*" * 40)
print(f"The value of 'true_value' is {true_value}")
print(f"The type of 'true_value' is: {type(true_value)}\n")
print(f"The value of 'false_value' is {false_value}")
print(f"The type of 'false_value' is: {type(false_value)}\n")
print("Using booleans in arithmetic operations")
print("*" * 40)
print(f"True + True = {true_value + true_value}")
print(f"True + False = {true_value + false_value}")
print(f"False + False = {false_value + false_value}")
print(f"False + n(5) = {false_value + n}")
print(f"True + a(8) = {true_value + a}")
print(f"True x n(5) = {true_value + a}")
print(f"(n < a) x 10 + (n == a) x 20 is: {(n < a) * 10 + (n == a) * 20}")
