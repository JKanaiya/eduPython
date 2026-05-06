# Python script to demonstrate function documentation generation and dynamic programming
# using introspection.

def add(a, b):
    """
    Calculates the sum of two numbers.
    :param a(int, float): The first number.
    :param b(int, float): The second number.
    :returns:
        int, float: The sum of two numbers. Return type depends on the type of input.

    Examples:
        >>> add(1, 2)
        3
        >>> add(3, 4.5)
        7.5
        >>> add(2.5, 3.1)
        5.6

    Notes:
        - The function can handle both floats and integers.
        - The result type will match the type of the inputs. For example, adding an integer to a float will
          yield a float
        - If either `a` or `b` are non-numeric type, a `TypeError` is raised.

    Raises:
        TypeError: If both `a` and `b` are non-numeric types.
    """
    return a + b


# Display the documenttion string of the add() function
print(f"The documentation string of the 'add()' function is given below:\n{add.__doc__}")


# Function to accept an arithemtic operator and two numbers to perform the operation on
def perform_operation(operation, x, y):
    """
    Performs a basic arithmetic operation ('add', 'subtract', 'multiply', 'divide') on two numbers.
    :param operation: A string indicating the type of arithmetic operation to be performed.
                      Accepted values are 'add', 'subtract', 'multiply' and 'divide'. (case insensitive.)
    :type operation: str
    :param x: The first number.
    :type x: int or float
    :param y: The second number.
    :type y: int or float
    :raises ValueError: If `operation` is not a strings.
    :raises ZeroDivisionError: If division by zero is attempted.

    :examples:
        >>> perform_operation('add', 1, 2)
        3
        >>> perform_operation('subtract', 1, 2)
        -1
        >>> perform_operation('multiply', 1, 2)
        2
        >>> perform_operation('divide', 9, 3)
        3.0

    :notes:
        - The operation string is case-insensitive.
        - Both integer and floating point numbers are accepted / supported.
        - If `y` is 0 (zero) and the operation is divide, a zero division error will be raised
    """
    if operation.lower() == "add":
        return x + y  # add(x, y)
    elif operation.lower() == "subtract":
        return x - y
    elif operation.lower() == "multiply":
        return x * y
    elif operation.lower() == "divide":
        return x / y
    else:
        raise ValueError(
            f"Operation '{operation.lower()}' is not recognized.\nPlease select one from the options below:\n1. add\n2. subtract\n3. multiply\n4. divide")

# Use global(s) to dynamically access and execute the operation() function
operation, num1, num2 = "add", 3, 5
print(f"Result of operation: {operation} on {num1} and {num2} is:\n{perform_operation(operation, num1, num2)}")

operation = input("Please enter the operation you would like to perform\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
num1 = int(input("Please enter the first number\n"))
num2 = int(input("Please enter the second number\n"))

# Perform the operation and display the result
print(f"Result operation: {operation} on {num1} and {num2} is:\n {perform_operation(operation, num1, num2)}")
