# This script demonstrates Python's selection / decision / conditional constructs
import sys

# Import the sys (system) module

# 1. if
temperature = float(input("Please enter today's temperature in degrees celcius: "))
if temperature > 25:
    print("☁ Its not that hot")

password = "idkidkidk"
if password == "":
    print("Please enter your password")

# 2.
user_num = int(input("Enter a number and i will tell you if its odd or even: "))
if user_num % 2 == 0:
    print(f"{user_num} is an even number")
else:
    print(f"{user_num} is an odd number")

score = int(input("Please enter your score: "))
if score >= 40:
    print("You have passed!")
else:
    print("You have failed!")

# 3. if...elif(else if)...else
# Grade the student based on their score entered above
if score >= 70 and score <= 100:
    print("You have passed with an A!")
elif score >= 60 and score <= 69:
    print("You have passed with a B!")
elif score >= 50 and score <= 59:
    print("You have passed with a C!")
elif score >= 40 and score <= 49:
    print("You have passed with a D!")
elif score >= 0 and score <= 39:
    print("You have failed with a F!")
else:
    print(f"Sorry {score} is not a valid number!")
    sys.exit()

# 4. match
# match works in python > 3.10 only
# it's similar to switch in the C programming language and its derivative languages
# Prompt the user for the day of the week
day = input("Please enter a day of the week: ")
match day.lower():
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print(f"{day.capitalize()} is weekday")
    case "saturday" | "sunday":
        print(f"{day.capitalize()} is weeend")
    case _:
        print(f"Sorry {day} is not a valid day")
        sys.exit()

# Give the student a comment based on their score in the exam using match
match score:
    case score if score >= 70:
        print("Excellent job!")
    case score if score >= 60:
        print("Not bad...")
    case score if score >= 50:
        print("Not good...")
    case score if score >= 40 and score >= 0:
        print("hehe...")
    case _:
        print(f"Sorry {score} is not a valid score")
        sys.exit()

