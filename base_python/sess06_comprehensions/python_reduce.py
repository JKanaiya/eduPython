# Python file / script to demonstrate the reduce() function

# Import the reduce() function from the functools module
from functools import reduce

# A list of numbers to maipulate using the reduce function
numbers = [17, 45, 23, 68, 144, 8, 51]

# Get the largest number from the numbers list using the reduce function
largets_num = reduce(lambda x, y: max(x, y), numbers)

# Get the least number from the numbers list using the reduce() function
smallest_num = reduce(lambda x, y: min(x, y), numbers)

# Obtain the product of all numbers using reduce() function
product_of_numbers = reduce(lambda x, y: x * y, numbers)

# Obtain the sum of all the numbers using the reduce() function
sum_of_nums = reduce(lambda x, y: x + y, numbers)

# Display the result
print(f"The list of numbers: {numbers}")
print(f"The largest number from the list: {largets_num}")
print(f"The smallest number form the list: {smallest_num}")
print(f"The product of numbers in the list: {product_of_numbers}")
print(f"The sum of numbers in the list: {sum_of_nums}")
