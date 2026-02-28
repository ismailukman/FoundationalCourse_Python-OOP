#!/usr/bin/env python

# =============================================================================
# MODULE 04: METHODS - INSTANCE, CLASS, AND STATIC - EXERCISES
# =============================================================================
# Test your understanding of the three method types.
# =============================================================================


# ---- Exercise 1: Classify the Methods ----
# For each method below, identify if it should be an instance method,
# class method, or static method. Add the appropriate decorator.

class Temperature:
    scale = "Celsius"  # Default scale

    def __init__(self, degrees):
        self.degrees = degrees

    # What type? Add decorator if needed.
    def display(self):
        print(f"{self.degrees}° {Temperature.scale}")

    # What type? Should change the scale for ALL temperatures.
    def set_scale(cls, new_scale):
        cls.scale = new_scale

    # What type? Pure conversion, no instance or class data needed.
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32

# YOUR CORRECTIONS HERE (add @classmethod and @staticmethod where needed):




# ---- Exercise 2: Alternative Constructor ----
# Create a class 'Date' with:
#   - __init__ takes year, month, day
#   - Class method from_string(date_str) parses "DD-MM-YYYY" format
#   - Class method today() returns today's date
#   - Instance method display() prints formatted date
# Test with: Date.from_string("25-12-2025")

# YOUR CODE HERE:




# ---- Exercise 3: Static Method Utility ----
# Create a class 'Validator' with only static methods:
#   - is_valid_email(email) -> True if contains '@' and '.'
#   - is_valid_age(age) -> True if 0 <= age <= 150
#   - is_strong_password(pwd) -> True if len >= 8, has upper, lower, digit

# YOUR CODE HERE:




# ---- Exercise 4: Predict the Output ----
# What will each line print?

class Counter:
    total = 0

    def __init__(self, name):
        self.name = name
        self.count = 0

    def increment(self):
        self.count += 1
        Counter.total += 1

    @classmethod
    def get_total(cls):
        return cls.total

    @staticmethod
    def describe():
        return "I count things!"

c1 = Counter("A")
c2 = Counter("B")

c1.increment()
c1.increment()
c2.increment()

# Prediction: ___
print(c1.count)

# Prediction: ___
print(c2.count)

# Prediction: ___
print(Counter.get_total())

# Prediction: ___
print(c1.describe())

# Prediction: ___
print(Counter.describe())


# ---- Exercise 5: Build a Complete Class ----
# Create a class 'BankAccount' with:
#   - Class variable: interest_rate = 0.02 (2%)
#   - Instance method: deposit(amount), withdraw(amount), get_balance()
#   - Class method: set_interest_rate(rate)
#   - Class method: from_dict(data) where data = {"owner": ..., "balance": ...}
#   - Static method: validate_amount(amount) -> True if positive number
#   - Instance method: apply_interest() -> adds interest to balance

# YOUR CODE HERE:




# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: set_scale -> @classmethod, celsius_to_fahrenheit -> @staticmethod
#
# Exercise 2: @classmethod; def from_string(cls, date_str):
#                 day, month, year = date_str.split('-')
#                 return cls(int(year), int(month), int(day))
#
# Exercise 3: All methods are @staticmethod since they don't need self or cls
#
# Exercise 4: c1.count=2, c2.count=1, total=3, describe works on both
#
# Exercise 5: Combine all three method types in one cohesive class
# =============================================================================
