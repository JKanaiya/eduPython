# Python script to demonstrate creating multiple threads to display numbers and letters

# Import the required module(s)
import threading

# Function to display numbers (to be run in a seperate thread)
def print_numbers():
    for i in range(1, 11):
        print(f"From thread1: i = {i}")

# Function to display letters (to be run in another seperate thread)
def print_letters():
    for letter in 'abcdefghij':
        print(f"From thread2: letter = {letter}")

# Create thread objects and start them
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()