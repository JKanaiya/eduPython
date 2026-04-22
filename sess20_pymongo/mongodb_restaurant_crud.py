# Script/file to demonstrate connecting a python app to mongodb
# NB: Ensure that the mongodb driver is installed

# Import the required modules
import pprint
from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ADSE_Restaurant"]

menu_col = db["menu"]
customers_col = db["customers"]
orders_col = db["orders"]


# --------------------------------------------------------------
# CREATE OPERATIONS
# --------------------------------------------------------------


# Function to add a menu idem
def add_menu_item():
    item = {
        "name": "Pizza",
        "category": "Food",
        "sizes": [
            {"size": "small", "price_kes": 500},
            {"size": "medium", "price_kes": 800},
            {"size": "large", "price_kes": 1200},
        ],
    }
    result = menu_col.insert_one(item)
    print(f"Menu item with id: {result.inserted_id} successfully added")


def add_customer(name, phone, email):
    customer = {
        "name": name,
        "phone": phone,
        "email": email,
    }
    result = customers_col.insert_one(customer)
    print(f"Customer with id: {result.inserted_id} successfully added")


def create_order(customer_id):
    order = {
        "customer_id": customer_id,
        "items": [
            {
                "name": "Pizza",
                "size": "medium",
                "quantity": 1,
                "price": 800,
            }
        ],
        "total_kes": 800,
        "status": "pending",
        "created_at": datetime.utcnow(),
    }
    result = orders_col.insert_one(order)
    print(f"Order with id: {result.inserted_id} successfully added")


# --------------------------------------------------------------
# READ OPERATIONS
# --------------------------------------------------------------


def view_menu():
    print("\nMenu")
    for item in menu_col.find():
        print(item)


def view_customers():
    print("\nCustomers: ")
    for customers in customers_col.find():
        print(customers)


def view_orders():
    print("\nOrders: ")
    for order in orders_col.find():
        print(order)


# --------------------------------------------------------------
# UPDATE OPERATIONS
# --------------------------------------------------------------


def update_order_status(order_id, new_status):
    result = orders_col.update_one({"_id": order_id}, {"$set": {"status": new_status}})
    print(f"Orders updated: {result.modified_count}")


# --------------------------------------------------------------
# DELETE OPERATIONS
# --------------------------------------------------------------


def delete_customer(customer_id):
    result = customers_col.delete_one({"_id": ObjectId(customer_id)})
    pprint.pp(f"Customers deleted: {result.deleted_count}")


# --------------------------------------------------------------
#  Entry point to our app
# --------------------------------------------------------------

if __name__ == "__main__":
    # 1. add a menu item
    # add_menu_item()

    # 2. add a customer
    # customer_id = add_customer("Alice", "07987654321", "alice@fakemail.com")

    # 3. create an order
    # create_order(customer_id)

    # 4. read data
    view_menu()
    view_customers()
    view_orders()

    # NB. for update/delete, copy an ID from printed out and then paste below
    # delete_customer("69c282c5842716a391790e3e")
