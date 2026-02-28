#!/usr/bin/env python

# =============================================================================
# MODULE 01: CLASSES AND INSTANCES - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Vehicle Class ----
# Create a class 'Vehicle' with attributes: name, max_speed, mileage
# Create an instance: Vehicle("Toyota Camry", 220, 15)
# Print: "Toyota Camry | Speed: 220 km/h | Mileage: 15 km/l"
#
# Expected Output:
# Toyota Camry | Speed: 220 km/h | Mileage: 15 km/l

# YOUR CODE HERE:




# ---- Question 2: Bank Account ----
# Create a class 'BankAccount' with:
#   - Attributes: owner (string), balance (float, default=0)
#   - Method: deposit(amount) -> adds amount to balance, prints new balance
#   - Method: withdraw(amount) -> subtracts if sufficient funds, else prints error
#   - Method: get_balance() -> returns current balance
#
# Expected Output:
# Account owner: Alice
# Deposited 500. New balance: 500.00
# Deposited 300. New balance: 800.00
# Withdrew 200. New balance: 600.00
# Insufficient funds! Balance: 600.00, Attempted: 1000
# Final balance: 600.00

# YOUR CODE HERE:




# ---- Question 3: Temperature Converter ----
# Create a class 'Temperature' with:
#   - Attribute: celsius (float)
#   - Method: to_fahrenheit() -> returns celsius * 9/5 + 32
#   - Method: to_kelvin() -> returns celsius + 273.15
#   - Method: display() -> prints all three values
#
# Create an instance with celsius=100 and call display()
#
# Expected Output:
# Celsius: 100.00
# Fahrenheit: 212.00
# Kelvin: 373.15

# YOUR CODE HERE:




# ---- Question 4: Shopping Item ----
# Create a class 'Item' with:
#   - Attributes: name, price, quantity
#   - Method: total_cost() -> returns price * quantity
#   - Method: apply_discount(percent) -> reduces price by given percentage
#   - Method: summary() -> returns formatted string
#
# Expected Output:
# Item: Laptop | Price: $999.99 | Qty: 2 | Total: $1999.98
# After 10% discount:
# Item: Laptop | Price: $899.99 | Qty: 2 | Total: $1799.98

# YOUR CODE HERE:




# ---- Question 5: Student Gradebook ----
# Create a class 'StudentRecord' with:
#   - Attributes: name, scores (a list of numbers)
#   - Method: average() -> returns the average of scores
#   - Method: highest() -> returns the highest score
#   - Method: lowest() -> returns the lowest score
#   - Method: report() -> prints a full report
#
# Expected Output:
# Student: Emma
# Scores: [85, 92, 78, 95, 88]
# Average: 87.60
# Highest: 95
# Lowest: 78

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS (try solving first!)
# =============================================================================

# # Question 1:
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# v = Vehicle("Toyota Camry", 220, 15)
# print(f"{v.name} | Speed: {v.max_speed} km/h | Mileage: {v.mileage} km/l")


# # Question 2:
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance:.2f}")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance:.2f}")
#         else:
#             print(f"Insufficient funds! Balance: {self.balance:.2f}, Attempted: {amount}")
#
#     def get_balance(self):
#         return self.balance
#
# acc = BankAccount("Alice")
# print(f"Account owner: {acc.owner}")
# acc.deposit(500)
# acc.deposit(300)
# acc.withdraw(200)
# acc.withdraw(1000)
# print(f"Final balance: {acc.get_balance():.2f}")


# # Question 3:
# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius
#
#     def to_fahrenheit(self):
#         return self.celsius * 9/5 + 32
#
#     def to_kelvin(self):
#         return self.celsius + 273.15
#
#     def display(self):
#         print(f"Celsius: {self.celsius:.2f}")
#         print(f"Fahrenheit: {self.to_fahrenheit():.2f}")
#         print(f"Kelvin: {self.to_kelvin():.2f}")
#
# t = Temperature(100)
# t.display()


# # Question 4:
# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total_cost(self):
#         return self.price * self.quantity
#
#     def apply_discount(self, percent):
#         self.price = round(self.price * (1 - percent / 100), 2)
#
#     def summary(self):
#         return f"Item: {self.name} | Price: ${self.price} | Qty: {self.quantity} | Total: ${self.total_cost()}"
#
# item = Item("Laptop", 999.99, 2)
# print(item.summary())
# print("After 10% discount:")
# item.apply_discount(10)
# print(item.summary())


# # Question 5:
# class StudentRecord:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores
#
#     def average(self):
#         return sum(self.scores) / len(self.scores)
#
#     def highest(self):
#         return max(self.scores)
#
#     def lowest(self):
#         return min(self.scores)
#
#     def report(self):
#         print(f"Student: {self.name}")
#         print(f"Scores: {self.scores}")
#         print(f"Average: {self.average():.2f}")
#         print(f"Highest: {self.highest()}")
#         print(f"Lowest: {self.lowest()}")
#
# s = StudentRecord("Emma", [85, 92, 78, 95, 88])
# s.report()
