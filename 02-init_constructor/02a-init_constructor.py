#!/usr/bin/env python

# =============================================================================
# MODULE 02: THE __init__ CONSTRUCTOR (Beginner)
# =============================================================================
#
# GOALS:
#   1. Understand what __init__ is and why it's called a "constructor"
#   2. Learn how self works inside __init__
#   3. Use default parameter values in __init__
#   4. Understand attribute initialisation from parameters
#   5. Create computed/derived attributes in __init__
#
# The __init__() method is a special method that Python calls automatically
# when you create a new instance of a class. It "initialises" the object
# with starting values. The double underscores (__) indicate it's a
# "magic" or "dunder" (double underscore) method.
#
# =============================================================================

# ---- Example 1: Basic __init__ ----
# Without __init__, you'd have to set each attribute manually

class PersonNoInit:
    pass

p = PersonNoInit()
p.name = "Alice"         # Setting attributes manually - tedious!
p.age = 30
print(f"{p.name}, age {p.age}")

# With __init__, attributes are set automatically at creation
class Person:
    def __init__(self, name, age):
        self.name = name    # 'self.name' is the attribute, 'name' is the parameter
        self.age = age

p = Person("Alice", 30)    # __init__ is called automatically here
print(f"{p.name}, age {p.age}")


# ---- Example 2: What is 'self'? ----
# 'self' refers to the specific instance being created/used.
# When you write Person("Alice", 30), Python internally does:
#   Person.__init__(new_object, "Alice", 30)
# So 'self' = the new_object being created

class Demonstrator:
    def __init__(self, value):
        print(f"__init__ called! self is: {self}")
        print(f"Setting value to: {value}")
        self.value = value

d = Demonstrator(42)
print(f"The object d is: {d}")    # Same memory address as 'self' above!


# ---- Example 3: Default Parameter Values ----
# You can give parameters default values so they're optional

class Employee:
    def __init__(self, name, department="General", salary=50000):
        self.name = name
        self.department = department
        self.salary = salary

    def info(self):
        return f"{self.name} | Dept: {self.department} | Salary: ${self.salary:,}"

# Using all defaults
e1 = Employee("John")
print(e1.info())   # John | Dept: General | Salary: $50,000

# Overriding some defaults
e2 = Employee("Sarah", "Engineering", 85000)
print(e2.info())   # Sarah | Dept: Engineering | Salary: $85,000

# Using keyword arguments to skip some parameters
e3 = Employee("Mike", salary=70000)
print(e3.info())   # Mike | Dept: General | Salary: $70,000


# ---- Example 4: Computed/Derived Attributes ----
# You can create attributes that are calculated from other attributes

class EmailUser:
    def __init__(self, first_name, last_name, domain="company.com"):
        self.first_name = first_name
        self.last_name = last_name
        self.domain = domain
        # Derived attributes - computed from other attributes
        self.full_name = f"{first_name} {last_name}"
        self.email = f"{first_name.lower()}.{last_name.lower()}@{domain}"

user = EmailUser("Corey", "Schafer")
print(f"Name: {user.full_name}")
print(f"Email: {user.email}")


# ---- Example 5: Validation in __init__ ----
# You can add logic to validate data when creating an instance

class Age:
    def __init__(self, years):
        if years < 0:
            raise ValueError("Age cannot be negative!")
        if years > 150:
            raise ValueError("Age seems unrealistic!")
        self.years = years

    def category(self):
        if self.years < 13:
            return "Child"
        elif self.years < 20:
            return "Teenager"
        elif self.years < 65:
            return "Adult"
        else:
            return "Senior"

a1 = Age(25)
print(f"Age {a1.years}: {a1.category()}")    # Age 25: Adult

a2 = Age(8)
print(f"Age {a2.years}: {a2.category()}")    # Age 8: Child

# Uncomment to see validation in action:
# a3 = Age(-5)   # Raises ValueError: Age cannot be negative!


# ---- Example 6: Initialising Collections in __init__ ----
# Be careful with mutable default arguments!

class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs if songs is not None else []  # Safe way!
        # WRONG: def __init__(self, name, songs=[])
        # Mutable defaults are shared across all instances!

    def add_song(self, song):
        self.songs.append(song)

    def show(self):
        print(f"Playlist: {self.name}")
        for i, song in enumerate(self.songs, 1):
            print(f"  {i}. {song}")

p1 = Playlist("Road Trip")
p1.add_song("Bohemian Rhapsody")
p1.add_song("Hotel California")
p1.show()

p2 = Playlist("Workout", ["Eye of the Tiger", "Stronger"])
p2.add_song("Lose Yourself")
p2.show()


# KEY TAKEAWAYS:
# - __init__ is called automatically when creating an instance
# - 'self' refers to the instance being created
# - Use default parameters to make arguments optional
# - You can compute derived attributes inside __init__
# - Validate data in __init__ to ensure objects start in a valid state
# - NEVER use mutable objects (lists, dicts) as default parameter values
