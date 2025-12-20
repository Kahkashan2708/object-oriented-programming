
---

##  Encapsulation

```python
"""
Encapsulation in Python
This file demonstrates data hiding and controlled access
using private variables and public methods.
"""

# Example 1: Encapsulation using private variables

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder   # public
        self.__balance = balance               # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# Creating an object
account = BankAccount("Kahkashan", 5000)

# Accessing data safely
account.deposit(1000)
print("Balance:", account.get_balance())

account.withdraw(2000)
print("Balance:", account.get_balance())

# Direct access is not allowed
# print(account.__balance)  # This will raise an error


# Example 2: Encapsulation with validation

class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100")

    def get_marks(self):
        return self.__marks


s = Student()
s.set_marks(95)
print("Marks:", s.get_marks())

s.set_marks(150)  # Invalid input

