# Python script to demonstrate function decorators

# Function to get nth Fibonacci number using recursion
def fibonacci(n):
    """
    Calculates the nth fibonacci number using recursion

    :param n: The nth fibonacci number

    :return: The nth fibonacci number
    """
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci() function decorator
def fib_decorator(func):
    """
    Decorator function that adds a print() statement before and after executing the decorated function

    :param func: The function to decorate

    :return: The decorated function
    """

    def wrapper(n):
        print("Calculating the Fibonacci numbers...")
        result = func(n)
        print("Fibonacci nmbers calculated")
        return result
    return wrapper

# Make use of the above decorator
@fib_decorator
def generate_fibonacci_numbers(n):
    """
    Generate a list of nth fibonacci numbers up to the value of n using the fibonacci decorator

    :param n: The nth fibonacci number

    :param n(int): The count of the fibonacci number.

    :returns (list): A list of fibonacci numbers
    """
    return [fibonacci(a) for a in range(n)]

# Call / invoke the generate_fibonaci_numbers() function to get the first 7 Fibonacci numbers
print(generate_fibonacci_numbers(7))