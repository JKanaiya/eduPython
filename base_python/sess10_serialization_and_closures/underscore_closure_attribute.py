# Python script to demonstrate the __closure__ attribute to access closure variables

def outer_func(outer_var):
    """
    Outer function that defines an inner function and captures
    the variable `outer_var` in its closure.

    Args:
        outer_var (int): A variable to be captured by the inner function.

    Returns:
        function: An inner function that uses the captured variable.
    """
    def inner_func(inner_var):
        return inner_var + outer_var
    return inner_func

# Create a closure by calling the outer function
closure_func = outer_func(10)

# Display the '__closure__' attribute of the closure function
print(f"Closure func's __closure__ attribute is: {closure_func.__closure__}")

# Demonstrate the use of the closure_func
result = closure_func(5)
print(f"The result of calling closure_func() with argument 5 is: {result}")

# Access the captured variable for the closure's cell
if closure_func.__closure__:
    captured_cell = closure_func.__closure__[0]
    captured_Value = captured_cell.cell_contents
    print(f"The captured value is: {captured_Value}")