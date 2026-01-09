# Python script to demonstrate creating a factorial function and its unit test

def factorial(n):
    """     Calculate the factorial of a non-negative integer.
    The factorial of a non-negative integer `n` is the product of all positive integers less
    than or equal to `n`.
    It is denoted by `n!` and is defined as:     - `0!` is 1 by definition.
    - For positive integers, `n! = n * (n - 1) * ... * 1`.
    This function uses recursion to compute the factorial. It raises an exception if t
    he input is negative,as the factorial is not defined for negative numbers.
    Parameters:
       n (int): A non-negative integer whose factorial is to be computed.
    Returns:
       int: The factorial of the integer `n`.
    Raises:     ValueError: If `n` is a negative integer, as factorials are not defined
                   for negative numbers.
    Example:
       >>> factorial(5)     120
       >>> factorial(0)     1
       >>> factorial(3)     6
    Notes:     - The function will raise a `RecursionError` if the recursion depth is
          exceeded for very large values of `n`.
          - This implementation may not be efficient for very large values of `n` due to deep recursion.
    """
    if n < 0:
        raise ValueError("You cannot calculate the factorial for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)