# Python script to demonstrate working with assertions

# Function to divide 2 numbers then return the quotient
def divide(x, y):
    assert y != 0, "Cannot divide by zero!" # Raise an AssertionError when y (denominator) is zero
    return x / y

try:
    result = divide(10, 2)
    print(f"10 / 2 = {result}")
    result = divide(10, 0)
    print(f"10 / 0 = {result}")
except AssertionError as ae:
    print(f"AssertionError: {ae}")

# Use an assertion for post condition check
def factorial(n):
    assert n > 0, "Negative numbers dont have factorial!"
    if n == 0 | n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get the factorial of 5 and -3
try:
    print(f"Factorial of 5 is {factorial(5)}") # Expected output is 120
    print(f"Factorial of 3 is {factorial(-3)}") # Raises an assertion error
except AssertionError as ae:
    print(f"AssertionError: {ae}")

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    try:
        assert len(numbers) > 0, "Cannot calculate the average of an empty list"
        average = sum(numbers) / len(numbers)
        print(f"The avergae of {numbers} is {average}")
        return average
    except AssertionError as ae:
        print(f"AssertionError: {ae}")
# Test the function with a non-empty and empty list
calculate_average([1, 2, 3, 4, 5])
calculate_average([])