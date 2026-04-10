#!/usr/bin/env python

# =============================================================================
# MODULE 04: METHODS - INSTANCE, CLASS, AND STATIC (Intermediate)
# =============================================================================
#
# GOALS:
#   1. Understand the three types of methods in Python classes
#   2. Learn when and why to use each type
#   3. Master @classmethod and @staticmethod decorators
#   4. Use class methods as alternative constructors
#   5. Understand how 'self' and 'cls' differ
#
# THREE TYPES OF METHODS:
#   - Instance methods: operate on instance data, take 'self' as first param
#   - Class methods:    operate on class data, take 'cls' as first param
#   - Static methods:   no access to instance or class data, utility functions
#
# =============================================================================

# ---- Example 1: Instance Methods (the default) ----
# Instance methods can access and modify instance AND class data via self
print("\nExample 1") 
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # Instance method - takes 'self', can access instance data
    def fullname(self):
        return f"{self.first} {self.last}"

    # Instance method - can also access class variables via self
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

e = Employee("Alice", "Smith", 70000)
print(e.fullname())         # Alice Smith
e.apply_raise()
print(f"New pay: ${e.pay:,}")  # New pay: $72,800


# ---- Example 2: Class Methods (@classmethod) ----
# Class methods receive the CLASS as the first argument, not the instance.
# They can modify class-level data that applies to all instances.
print("\nExample 2") 
class Employee2:
    raise_amount = 1.04
    num_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee2.num_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    @classmethod
    def set_raise_amount(cls, amount):
        """Modifies the raise_amount for ALL employees."""
        cls.raise_amount = amount    # 'cls' = the class itself

    @classmethod
    def get_employee_count(cls):
        return cls.num_employees

print(f"\nRaise amount before: {Employee2.raise_amount}")  # 1.04
Employee2.set_raise_amount(1.06)
print(f"Raise amount after: {Employee2.raise_amount}")     # 1.06

e1 = Employee2("Bob", "Jones", 60000)
e2 = Employee2("Carol", "White", 80000)
print(f"Total employees: {Employee2.get_employee_count()}")  # 2


# ---- Example 3: Class Methods as Alternative Constructors ----
# A very common pattern: creating instances from different data formats
print("\nExample 3") 
class Employee3:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        """Create an Employee from a dash-separated string."""
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))  # cls() creates a new instance

    @classmethod
    def from_dict(cls, emp_dict):
        """Create an Employee from a dictionary."""
        return cls(emp_dict['first'], emp_dict['last'], emp_dict['pay'])

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

# Standard construction
e1 = Employee3("Alice", "Smith", 70000)
print(f"\nStandard: {e1}")

# From string (alternative constructor)
e2 = Employee3.from_string("Bob-Jones-60000")
print(f"From string: {e2}")

# From dictionary (alternative constructor)
data = {"first": "Carol", "last": "White", "pay": 85000}
e3 = Employee3.from_dict(data)
print(f"From dict: {e3}")


# ---- Example 4: Static Methods (@staticmethod) ----
# Static methods don't receive 'self' or 'cls'. They're utility functions
# that logically belong to the class but don't need instance/class data.
print("\nExample 4") 
class DateUtils:
    @staticmethod
    def is_workday(day):
        """Check if a day (0=Mon, 6=Sun) is a workday."""
        return day.weekday() not in (5, 6)  # 5=Sat, 6=Sun

    @staticmethod
    def days_between(date1, date2):
        """Get the number of days between two dates."""
        return abs((date2 - date1).days)

import datetime

today = datetime.date.today()
print(f"\nIs today a workday? {DateUtils.is_workday(today)}")

date1 = datetime.date(2025, 1, 1)
date2 = datetime.date(2025, 12, 31)
print(f"Days in 2025: {DateUtils.days_between(date1, date2)}")


# ---- Example 5: When to Use Which? ----
print("\nExample 5") 
class MathHelper:
    precision = 2  # Class variable

    def __init__(self, value):
        self.value = value

    # INSTANCE METHOD: needs access to self.value
    def round_value(self):
        return round(self.value, MathHelper.precision)

    # CLASS METHOD: needs to modify class-level config
    @classmethod
    def set_precision(cls, digits):
        cls.precision = digits

    # STATIC METHOD: pure utility, no need for self or cls
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathHelper.factorial(n - 1)

m = MathHelper(3.14159)
print(f"\nRounded: {m.round_value()}")           # 3.14

MathHelper.set_precision(4)
print(f"New precision: {m.round_value()}")        # 3.1416

print(f"Is 7 even? {MathHelper.is_even(7)}")     # False
print(f"5! = {MathHelper.factorial(5)}")          # 120


# ---- Example 6: Complete Real-World Example ----

class Pizza:
    sizes = {"S": 8, "M": 12, "L": 16}   # Diameter in inches

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    # Instance method
    def description(self):
        top_str = ", ".join(self.toppings) if self.toppings else "Plain"
        return f"{self.size}-inch pizza with {top_str}"

    # Class method as alternative constructor
    @classmethod
    def margherita(cls, size="M"):
        return cls(cls.sizes[size], ["Mozzarella", "Tomato", "Basil"])

    @classmethod
    def pepperoni(cls, size="M"):
        return cls(cls.sizes[size], ["Mozzarella", "Pepperoni"])

    # Static method - utility
    @staticmethod
    def calculate_price(diameter, num_toppings):
        base = diameter * 0.75
        return base + (num_toppings * 1.50)

print("\n--- Pizza Shop ---")
p1 = Pizza.margherita("L")
print(p1.description())
price = Pizza.calculate_price(p1.size, len(p1.toppings))
print(f"Price: ${price:.2f}")

p2 = Pizza.pepperoni()
print(p2.description())
price = Pizza.calculate_price(p2.size, len(p2.toppings))
print(f"Price: ${price:.2f}")


# KEY TAKEAWAYS:
# - Instance methods: take 'self', work with instance data → most common
# - Class methods: take 'cls', work with class data → config, alt constructors
# - Static methods: no self/cls, pure utility → helper functions
# - Use @classmethod for alternative constructors (from_string, from_dict, etc.)
# - Use @staticmethod for functions that logically belong to the class
#   but don't need access to instance or class state
