# Python script to demonstrate the use of instance, static, and class methods in a
# real world scenario

# Import the regular expressions method
import re


#

class BankAccount:
    # Class attribute (shared across all instances)
    interest_rate = 0.05  # 5% annual interest rate

    # Constructor
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # instance Method(s)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            # Display the new balance
            print(f"[{self.account_holder}] deposited Kes. {amount:.2f}"
                  f"\new balance is: Kes. {self.balance:.2f}")
        else:
            print(f"Kindly note: deposit amount must be greater than zero")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"[{self.account_holder}] withdrawn Kes. {amount:.2f}"
                  f"\nNew balance is: Kes. {self.balance:.2f}")
        else:
            print(f"Kindly note: withdraw amount must be greater than zero or insufficent funds")

    # Class method(s)
    @classmethod
    def set_interest(cls, new_rate):
        if 0 <= new_rate <= 0.2:
            cls.interest_rate = new_rate
            # Notify about the change in annual interest rate
            print(f"The annual interest rate has been set to {new_rate * 100:.2f}% for all accounts!")
        else:
            print(f"Kindly note: interest rate must be between 0% and 20%")

    # Static method
    @staticmethod
    def validate_account_number(account_number):
        pattern = r"^ACC\d{6}$" # Regular expression (regex), ACC followed by 6 digits
        return bool(re.match(pattern, account_number))


# Demonstrate the bank account class and its instance, class, and static methods

# Create 2 bank account objects

abigails_acc = BankAccount("ABIGAIL", 55000)
brian_acc = BankAccount("BRAIN", 15000)

# Deposit and withdraw money to and from the mhd and dhm account
abigails_acc.deposit(1500)
abigails_acc.withdraw(700)

# Update the annual interest rate from 5% to 8%
BankAccount.set_interest(0.08)

# Validate new account numbers => static method
print("Validating new account numbers...")
print("ACC123456 is valid?: ", BankAccount.validate_account_number("ACC123456"))


