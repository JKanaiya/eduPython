# Python script demonstrating how to import a module and use its code in the current script

# Import the code from the 'greetings' module
from greetings import greet

# Prompt the user for their name
username = input('What is your name? ')

# Use the function from the greetings module to greet the user
print(greet(username))