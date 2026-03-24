# Python script to demonstrate the use of closure to multiply a parameter with a second value

# Define the enclsing function
def multiplier(n):
    def inner(x):  # Enclosed function
        return x * n

    return inner


# Create 2 multiplier functions
triple = multiplier(3)
quadruple = multiplier(4)

# Use the above closures to triple 5 and quadriple 8
print(f"5 tripled is {triple(5)}")
print(f"8 quadruple is {quadruple(8)}")
print(f"bla")

