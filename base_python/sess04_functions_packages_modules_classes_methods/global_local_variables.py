# Python script to demonstrate the scop of global and local variables

# Declare a global variables
global_var = 5

# define a function to display the value passed to it
def display_value(value):
    print(f"The value passed is {value}")

# Call the display_value function and pass in the global variable
display_value(global_var)

def random_function():
    random_variable = "Hello" # random_variable is only accessible within random_function
    return random_variable

# Call the display value function and pass in the random variable
# display_value(random_variable) RAISES AND ERROR
