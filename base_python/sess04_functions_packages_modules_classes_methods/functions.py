# This file demonstrates defining& calling user defined funcitons in python
from sess02_python_data_types.python_arithmetic_operations import difference


# Define a function to display a greeting message when called / invoked
def greeting():  # does not take any parameters
    print(f"Hello from greetings.py")


# Invoke the greeting() function
greeting()


# Define a function that accepts the user's name and greets them
def greet_name(name):  # Accept's a single parameter
    print(f"Hello {name}")


# Prompt the user fro their name and invoke the greet_name funciton
username = input("Enter your name: \n")
greet_name(f"{username}")


# Create a function that accepts two numbers & an operator '+' (default) or 'x' to add
# or multiply them
def add_or_multiply(first_num, second_num, operator='+'):
    if operator == '+':
        print(f"{first_num} + {second_num} = {first_num + second_num}")
    elif operator == '*' or operator == 'x':
        print(f"{first_num} {operator} {second_num} = {first_num * second_num}")
    else:
        print("Invalid operator")


add_or_multiply(1, 2, '+')
add_or_multiply(5, 7, '-')
add_or_multiply(6, 6, '*')

# Display the documentation string for the add_or_multiply function
# print(f"{add_or_multiply.__doc__}")

# Anonymous function(s)
# An anonymous function is a way to write small compact functions quickly
# used when you need a simple function for a short period and dont want to write a full function
# using the def keyword
plus_five = lambda num: num + 5  # used a lambda to add 5 to a number
print(f"The sum of 7 and 5 using a lambda (anonymous) {plus_five(7)}")


# Same functionality as the lambda above but using a full function
def add_five(num):
    return num + 5


print(f"The sum of 7 and 5 using the full function: {add_five(7)}")

# Anonymous / lambda function to get the difference betwween 2 numbers
difference = lambda num1, num2: num1 - num2
print(f"The difference between the two numbers using lmabda: {difference(7, 5)}")


# Function with a varying number of parameter
# Define a function that accepts a varying number of arguments
# def get_sum(values):
#     sum = 0
#     for value in values:
#         sum += values
#     return value

def get_sum(*values):
    """
    This function return the sum of all the numeric values provided.

    Args:
        *values: Variable number of values to be totalled / summed

    Returns: int or float: The sum of all the numbers / values passed in as an integer / float

    Raises:
        TypeError: if any of the values / numbers are not numeric

    Examples:
        >>> get_sum(1, 2, 3)
        6
        >>> get_sum(1, 2, 3, 4)
        10
        >>> get_sum(1, 2, 3, 4, "3")
        TypeError: All the values provided must be numbers
    """
    try:
        return sum(values)
    except TypeError as e:
        raise  TypeError("All the values provided must be numbers") from e

# Create a list of numbers and sum them using the get_sum() function
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The sum of the first 10 numbers is: {get_sum(*num_list)}")

