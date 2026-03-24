# Python script to demonstrate the various arithmetic operations on numeric values
# Declare and get 2 values from the user
from math import floor

num1 = int(input("Enter the first number to be used in the calculation: \n"))
num2 = int(input("Enter the first number to be used in the calculation: \n"))

# Addition
sum = num1 + num2

# Subtraction
difference = num1 - num2

# Multiplication
product = num1 * num2

# Division
integer_division = num1 / num2
floor_division = num1 // num2

# Modulus
modulus = num1 % num2

# Exponentiation
exponent = num1**num2

# Display the results
print(f"Addition: {num1} + {num2} = {sum}")
print(f"Subtraction: {num1} - {num2} = {difference}")
print(f"Multiplication: {num1} * {num2} = {product}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")
print(f"Integer Division: {num1} /{num2} = {integer_division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponent: {num1} ** {num2} = {exponent}")

print(floor(4.5))
