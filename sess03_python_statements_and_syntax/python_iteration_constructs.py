# This script demonstrates Python's iteration / looping / repitition constructs

# 1. For loop
# Create a list of fruits
import pprint

fruits = [
    "kiwi",
    "watermelon",
    "pineapple",
    "strawberry",
    "banana",
    "mango",
    "blackberry",
    "blueberry",
    "grapes",
    "guava",
    "orange",
    "passion",
    "date",
    "tomato",
    "avocado",
    "apple",
    "plums",
    "cashewfruits",
    "dragonfruit",
    "lemon",
]

# Display each of the above fruits using a 'for' loop
for fruit in fruits:
    pprint.pp(f"The current fruit is: {fruit}")

# Create a list of numbers
numbers = [1, 3, 5, 12, 134, 56, 79, 38]
for num in numbers:
    pprint.pp(f"The current number is: {num}")

# 2. range
pprint.pp("range".center(42, "-"))

test = "------------------range-------------------"

# Basic range: generate first 5 numbers
for n in range(5):
    pprint.pp(f"The ccurrent number in the range is: {n}")

print("range with parameters".center(42, "-"))
# Generate even numbers starting from 2 to 10 (exclusive) using a range with staart, stop and step value
for n in range(2, 10, 2):
    pprint.pp(f"The ccurrent even number in the range is: {n}")

# Display the cubes of the first 5 integers using a ranged for loop and list comprehension
cubes = [n**3 for n in range(1, 6)]
pprint.pp("The cubes of the first 5 numbers are: {cubes}")

# 3. while loop
pprint.pp("while loop".center(42, "-"))
# Display the first  multiples of 8
n = 1
while n <= 5:
    pprint.pp(f"The {n} x 8 is: {n * 8}")
    pprint.pp("%d x 8 = %d" % (n, n * 8))
    n += 1

# Create a list of even numbers
n, even_nums = 1, []
pprint.pp("The even numbers between 1 - 20 are:")
while n <= 20:
    if n % 2 == 1:
        n += 1
        continue
    elif n % 2 == 0:
        even_nums.append(n)
        n += 1
# Display the list of even numbers
print(even_nums)

# Practical use of a while loop to search for some text in a paragraph
paragraph = """
Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code 
for the video you want to add. You can also type a keyword to search online for the video that best fits your document. 
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that 
complement each other.

For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want 
from the different galleries. Themes and styles also help keep your document coordinated. When you click Design and 
choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme.
""".lower()

# variable to hold the word / text to search for
word = "you".lower()
found = False
index = 0

while index < len(paragraph):
    # find the index of the word
    if paragraph[index : index + len(word)] == word:
        found = True
        break
    index += 1

if found:
    pprint.pp(f"The word {word} was found at index {index}")
else:
    pprint.pp(f"The word {word} was not found")
