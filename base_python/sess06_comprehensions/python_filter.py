# Python script to demonstrate the filter() function

# List of fibonacci numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Get and display a list of odd fibonacci numbers usin the filter
odd_fibonacci = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Fibonacci numbers: {numbers}")
print(f"Odd fibonacci numbers: {odd_fibonacci}")

# Set of student names
student_names = {
    "Abigail", "Bernice", "Charlene", "Denise", "Sue", "Jim", "Mark", "Micha",
    "William", "Jane", "Xi", "Alfred", "Hillary", "Anthony", "Birdig",
    "Mitchell", "Alice"}

# Use the filter() function to get and display the names starting with 'A'
filtered_names = list(filter(lambda name: name.startswith('A'), student_names))
print(f"All Student names: {student_names}")
print(f"All student names begining with 'A': {filtered_names}")


# Function to determine whether a number is a prime number or not
def is_prime(n):
    """
           Check if a given number is a prime number.



           A prime number is a natural number greater than 1 that has no positive divisors
           other than 1 and itself.



           Args:
           n (int): The number to be checked. Must be a non-negative integer.



           Returns:
           bool: True if the number is prime, False otherwise.



           Examples:
                > is_prime(1)
                       False
                > is_prime(2)
                       True
                > is_prime(3)
                       True
                > is_prime(4)
                       False
                > is_prime(29)
                       True
                > is_prime(100)
                       False
                > is_prime(97)
                       True



           Notes:
           - The function uses the square root to reduce the number of checks.
           - Negative numbers and numbers less than 2 are not considered prime.
           """

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # same as: [for i in range (wm nt()math.sqrt(n)) + 1]
        if n % i == 0:
            return False
    return True

# Set the range of number that we'd like to get prime numbers
num_range = range(1, 70)

prime_numbers = list(filter(lambda num: is_prime(num), num_range))
print(f"All prime numbers between 1 and 70: {prime_numbers}")
