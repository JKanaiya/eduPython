# Python file to demonstrate real life uses of closures

# Closure to calculate discount at a store
def discount_calculator(discount_percentage):
    def calculate(price):
        return price * (1 - discount_percentage / 100) # or price - (price * dicount_percentage / 100)
    return calculate

black_friday = discount_calculator(20)
christmas_sale = discount_calculator(30)
print(f"Normal price: Kes. 1000\nBlack Friday Deal: {black_friday(1000)}")
print(f"Normal price: Kes. 1000\nChristmas sale: {christmas_sale(1000)}")

# Closure for an email template generator
def email_template(name):
    greetings = f"Dear {name},\n"
    def format_message(body):
        return f"{greetings}{body}\nBest regards\n\nMHD"
    return format_message

# Use the email template closure to notify a student to collect their transcript
student_result = email_template("Muhammad Hasan")
print(f"{student_result('Please come and collect your transcript')}")

# Use the email template closure to request a supplier to deliver a product
supplier_reminder = email_template("Carre4")
print(f"{supplier_reminder('Please come and pay me my money')}")

# Inspect the above for __closure__
print(student_result.__closure__) # Tuple with one cell
print(student_result.__closure__[0].cell_contents) # "Dear Muhammad Hasan,"

print(supplier_reminder.__closure__) # Tuple with one cell
print(supplier_reminder.__closure__[0].cell_contents) # "Dear Carre4,"
