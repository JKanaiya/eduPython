# Python script to demonstrate how to read and display a JSON file and data

# Import the required modules
import json

# Open the 'burger_sales.json' file in read mode and display its content
with open("../files/burger_sales.json") as json_file:
    # Use a for loop to display the sales in the 'burger_sales.json' file
    burger_sales = json.load(json_file)
    for sale in burger_sales:
        print(sale)
        print(sale)
