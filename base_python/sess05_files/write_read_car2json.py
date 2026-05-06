# Python script to write car details (as dictionaries) to a json file and read them
# back for display

# Import the required modules
from pathlib import Path  # Allow our script to work with different Os's without \ or /
import json  # Allow our script to write and read JSOn format
from plistlib import loads


# Function to write car details
def save_car_detals(file_path: Path, car_list: list):
    """
    Saves a list of car dictionaries to a JSON file
    :param file_path: path to save file
    :param car_list: list of car dictionaries
    """
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(car_list, file, indent=4)
        print(f"✅ Car data succesfully sae to {file_path}")
    except Exception as e:
        print(f"Error occurred while saving car data:\n {e}")


# Function to load / read the car details from file
def display_car_details(file_path: Path) -> list:
    """
    Loads a list of car dictionaries from a JSON file

    :param file_path: path to save file
    :return: list of car dictionaries
    """
    try:
        with file_path.open('r', encoding="utf-8") as file:
            return json.load(file)
    # Handle the errors / exception
    except FileNotFoundError as fnf:
        print(f"File not found:\n {fnf}")
        return []
    except json.decoder.JSONDecodeError as jde:
        print(f"Failed to decode the JSON data:\n {jde}")
        return []
    except Exception as e:
        print(f"Failed to read car data:\n {e}")
        return []


# Functionto display the car details
def display_car_data(car_list: list):
    """
    Displays a list of car dictionaries

    :param car_list: list of car dictionaries
    :return: list of car dictionaries
    """
    if not car_list:
        print("Sorry, no car details were found.")
        return;
    print(f"\n🚗 Car details successfully displayed:")
    for car in car_list:
        print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, Price: {car['price']}")


# Define car details/data
cars = [
    {"make": "Toyota", "model": "Corolla", "year": 2020, "price": 2000000},
    {"make": "Honda", "model": "Civic", "year": 2021, "price": 2200000},
    {"make": "Ford", "model": "Mustang", "year": 2022, "price": 3500000},
    {"make": "Tesla", "model": "Model 3", "year": 2023, "price": 4000000},
    {"make": "Mazda", "model": "CX-5", "year": 2018, "price": 2400000},
    {"make": "Chevrolet", "model": "Malibu", "year": 2019, "price": 1800000},
    {"make": "BMW", "model": "X5", "year": 2022, "price": 5000000},
    {"make": "Audi", "model": "A4", "year": 2021, "price": 3800000},
    {"make": "Nissan", "model": "Altima", "year": 2020, "price": 2100000},
    {"make": "Hyundai", "model": "Elantra", "year": 2023, "price": 2500000}
]

# Define the path to save the 'cars.json' file i.e one drectory up into 'files/cars.json'
file_path = Path.cwd().parent / "files" / "cars.json"

# Call the earlier defined functions to 1. write / save, 2. Read and 3. Display the car details / data
save_car_detals(file_path, cars)
car_details = display_car_details(file_path)
display_car_data(car_details)
