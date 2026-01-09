# Python script to demonstrate how to handle multiple exceptions

try: # Code that may raise error(s) / exception(s)
    num_list = [3, 5, 8]
    # Try to display a number at an invalid index
    print(f"Value at index 7 is: {num_list[7]}")

    # Other possible exceptions
    num_list + 5 # Type error as you cannot sum an integer and a list

    num_list.remove(4) # Value error as the list doesnt contain a number 4

    # Attempt integer division by zero
    quotient = 12 / 0
except IndexError:
    print("Error: Invalid index")
except TypeError:
    print("TypeError: Cannot sum list and integer")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")
except ValueError:
    print("ValueError: Sorry the list doesnt contain the sepcified number")