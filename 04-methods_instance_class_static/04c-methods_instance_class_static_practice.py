#!/usr/bin/env python

# =============================================================================
# MODULE 04: METHODS - INSTANCE, CLASS, AND STATIC - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Employee Management ----
# Create a class 'Employee' with:
#   - Class var: raise_rate = 1.05, employee_count = 0
#   - Instance method: apply_raise(), full_info()
#   - Class method: set_raise_rate(rate), from_csv(csv_string)
#   - Static method: is_valid_pay(pay) -> True if pay > 0
#
# Expected Output:
# Employees: 2
# Alice Smith | Pay: $70,000
# Bob Jones | Pay: $60,000
# After 5% raise:
# Alice Smith | Pay: $73,500
# Setting raise rate to 10%...
# Bob Jones | Pay: $66,000
# From CSV: Carol White | Pay: $90,000
# Is $-5000 valid? False

# YOUR CODE HERE:




# ---- Question 2: Recipe Manager ----
# Create a class 'Recipe' with:
#   - Class var: all_recipes = []
#   - Instance: name, ingredients (list), servings
#   - Instance method: scale(factor) -> adjusts servings
#   - Class method: from_text(text) where text = "Name;ing1,ing2;servings"
#   - Class method: search(keyword) -> returns recipes containing keyword
#   - Static method: convert_cups_to_ml(cups) -> cups * 236.588
#
# Expected Output:
# Pancakes (Serves 4)
# Ingredients: flour, eggs, milk, sugar
# Scaled to 8 servings
# Waffles (Serves 6)
# Recipes with 'eggs': Pancakes, Waffles
# 2 cups = 473.18 ml

# YOUR CODE HERE:




# ---- Question 3: Logger System ----
# Create a class 'Logger' with:
#   - Class vars: log_level = "INFO", log_history = []
#   - Instance: module_name
#   - Instance method: log(message) -> formats and stores log
#   - Class method: set_level(level) -> changes log level for all
#   - Class method: get_history() -> returns all logged messages
#   - Static method: format_timestamp() -> returns current timestamp string
#
# Expected Output:
# [2026-02-27 INFO] [Auth] User logged in
# [2026-02-27 INFO] [Database] Query executed
# Setting level to WARNING...
# [2026-02-27 WARNING] [Auth] Failed login attempt
# Total log entries: 3

# YOUR CODE HERE:




# ---- Question 4: Shape Factory ----
# Create a class 'Shape' with class methods that act as factories:
#   - Class method: circle(radius) -> returns dict with type, area, perimeter
#   - Class method: rectangle(w, h) -> returns dict with type, area, perimeter
#   - Class method: triangle(a, b, c) -> returns dict with type, perimeter
#   - Static method: describe(shape_dict) -> prints shape info
#
# Expected Output:
# Type: circle | Area: 78.54 | Perimeter: 31.42
# Type: rectangle | Area: 24.00 | Perimeter: 20.00
# Type: triangle | Perimeter: 12.00

# YOUR CODE HERE:




# ---- Question 5: User Authentication ----
# Create a class 'User' with:
#   - Class vars: users = {}, min_password_length = 8
#   - Instance: username, _password_hash (store len of password as simple hash)
#   - Class method: register(username, password) -> creates & stores user
#   - Class method: login(username, password) -> validates credentials
#   - Class method: set_password_policy(min_len)
#   - Static method: hash_password(password) -> returns simple hash (len)
#   - Instance method: change_password(old_pw, new_pw) -> updates if old matches
#
# Expected Output:
# User 'alice' registered successfully
# User 'bob' registered successfully
# Registration failed: Password too short (min 8 chars)
# Login 'alice': Success!
# Login 'alice' with wrong password: Failed!
# Total registered users: 2

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# class Employee:
#     raise_rate = 1.05
#     employee_count = 0
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         Employee.employee_count += 1
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_rate)
#
#     def full_info(self):
#         return f"{self.first} {self.last} | Pay: ${self.pay:,}"
#
#     @classmethod
#     def set_raise_rate(cls, rate):
#         cls.raise_rate = rate
#
#     @classmethod
#     def from_csv(cls, csv_string):
#         first, last, pay = csv_string.split(',')
#         return cls(first.strip(), last.strip(), int(pay.strip()))
#
#     @staticmethod
#     def is_valid_pay(pay):
#         return pay > 0
#
# e1 = Employee("Alice", "Smith", 70000)
# e2 = Employee("Bob", "Jones", 60000)
# print(f"Employees: {Employee.employee_count}")
# print(e1.full_info())
# print(e2.full_info())
# print("After 5% raise:")
# e1.apply_raise()
# print(e1.full_info())
# print("Setting raise rate to 10%...")
# Employee.set_raise_rate(1.10)
# e2.apply_raise()
# print(e2.full_info())
# e3 = Employee.from_csv("Carol, White, 90000")
# print(f"From CSV: {e3.full_info()}")
# print(f"Is $-5000 valid? {Employee.is_valid_pay(-5000)}")


# # Question 2:
# class Recipe:
#     all_recipes = []
#
#     def __init__(self, name, ingredients, servings):
#         self.name = name
#         self.ingredients = ingredients
#         self.servings = servings
#         Recipe.all_recipes.append(self)
#
#     def scale(self, factor):
#         self.servings = int(self.servings * factor)
#         print(f"Scaled to {self.servings} servings")
#
#     def display(self):
#         print(f"{self.name} (Serves {self.servings})")
#         print(f"Ingredients: {', '.join(self.ingredients)}")
#
#     @classmethod
#     def from_text(cls, text):
#         name, ings, servings = text.split(';')
#         return cls(name, ings.split(','), int(servings))
#
#     @classmethod
#     def search(cls, keyword):
#         found = [r.name for r in cls.all_recipes if keyword in r.ingredients]
#         return found
#
#     @staticmethod
#     def convert_cups_to_ml(cups):
#         return cups * 236.588
#
# r1 = Recipe("Pancakes", ["flour", "eggs", "milk", "sugar"], 4)
# r1.display()
# r1.scale(2)
# r2 = Recipe.from_text("Waffles;flour,eggs,butter;6")
# r2.display()
# found = Recipe.search("eggs")
# print(f"Recipes with 'eggs': {', '.join(found)}")
# print(f"2 cups = {Recipe.convert_cups_to_ml(2):.2f} ml")


# # Question 3:
# from datetime import date
# class Logger:
#     log_level = "INFO"
#     log_history = []
#
#     def __init__(self, module_name):
#         self.module_name = module_name
#
#     def log(self, message):
#         entry = f"[{Logger.format_timestamp()} {Logger.log_level}] [{self.module_name}] {message}"
#         Logger.log_history.append(entry)
#         print(entry)
#
#     @classmethod
#     def set_level(cls, level):
#         cls.log_level = level
#
#     @classmethod
#     def get_history(cls):
#         return cls.log_history
#
#     @staticmethod
#     def format_timestamp():
#         return str(date.today())
#
# auth_logger = Logger("Auth")
# db_logger = Logger("Database")
# auth_logger.log("User logged in")
# db_logger.log("Query executed")
# print("Setting level to WARNING...")
# Logger.set_level("WARNING")
# auth_logger.log("Failed login attempt")
# print(f"Total log entries: {len(Logger.get_history())}")


# # Question 4:
# import math
# class Shape:
#     @classmethod
#     def circle(cls, radius):
#         return {"type": "circle", "area": math.pi*radius**2, "perimeter": 2*math.pi*radius}
#
#     @classmethod
#     def rectangle(cls, w, h):
#         return {"type": "rectangle", "area": w*h, "perimeter": 2*(w+h)}
#
#     @classmethod
#     def triangle(cls, a, b, c):
#         return {"type": "triangle", "perimeter": a+b+c}
#
#     @staticmethod
#     def describe(shape_dict):
#         parts = [f"Type: {shape_dict['type']}"]
#         if 'area' in shape_dict:
#             parts.append(f"Area: {shape_dict['area']:.2f}")
#         parts.append(f"Perimeter: {shape_dict['perimeter']:.2f}")
#         print(" | ".join(parts))
#
# Shape.describe(Shape.circle(5))
# Shape.describe(Shape.rectangle(4, 6))
# Shape.describe(Shape.triangle(3, 4, 5))


# # Question 5:
# class User:
#     users = {}
#     min_password_length = 8
#
#     def __init__(self, username, password):
#         self.username = username
#         self._password_hash = User.hash_password(password)
#
#     @classmethod
#     def register(cls, username, password):
#         if len(password) < cls.min_password_length:
#             print(f"Registration failed: Password too short (min {cls.min_password_length} chars)")
#             return None
#         user = cls(username, password)
#         cls.users[username] = user
#         print(f"User '{username}' registered successfully")
#         return user
#
#     @classmethod
#     def login(cls, username, password):
#         if username in cls.users:
#             if cls.users[username]._password_hash == cls.hash_password(password):
#                 print(f"Login '{username}': Success!")
#                 return True
#         print(f"Login '{username}' with wrong password: Failed!")
#         return False
#
#     @classmethod
#     def set_password_policy(cls, min_len):
#         cls.min_password_length = min_len
#
#     @staticmethod
#     def hash_password(password):
#         return len(password)
#
#     def change_password(self, old_pw, new_pw):
#         if User.hash_password(old_pw) == self._password_hash:
#             self._password_hash = User.hash_password(new_pw)
#             return True
#         return False
#
# User.register("alice", "password123")
# User.register("bob", "securepass")
# User.register("eve", "short")
# User.login("alice", "password123")
# User.login("alice", "wrongpw")
# print(f"Total registered users: {len(User.users)}")
