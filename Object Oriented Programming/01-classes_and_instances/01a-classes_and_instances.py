#!/usr/bin/env python

# =============================================================================
# MODULE 01: CLASSES AND INSTANCES (Beginner)
# =============================================================================
#
# GOALS:
#   1. Understand what a class is and why we use them
#   2. Learn how to create a basic class
#   3. Create instances (objects) from a class
#   4. Add attributes to instances manually
#   5. Understand the difference between a class and an instance
#
# A class is like a blueprint or template for creating objects. An instance
# is an actual object created from that blueprint. Think of a class as a
# cookie cutter, and each cookie you make is an instance.
#
# WHY USE CLASSES?
#   - Organise related data and behaviour together
#   - Avoid repeating code (DRY - Don't Repeat Yourself)
#   - Model real-world entities in your programs
#   - Make code more readable, maintainable, and reusable
#
# =============================================================================

# ---- Example 1: The Simplest Class ----
# A class with no attributes or methods (using 'pass' as a placeholder)

class Dog:
    pass

# Creating instances (objects) from the Dog class
dog1 = Dog()
dog2 = Dog()

print(dog1)  # <__main__.Dog object at 0x...>  (unique memory address)
print(dog2)  # <__main__.Dog object at 0x...>  (different memory address)

# Each instance is unique even though they come from the same class
print(dog1 == dog2)  # False - they are two different objects


# ---- Example 2: Adding Attributes to Instances Manually ----
# You can attach data to instances after creation (but this is not ideal)

dog1.name = "Buddy"
dog1.breed = "Golden Retriever"
dog1.age = 3

dog2.name = "Max"
dog2.breed = "German Shepherd"
dog2.age = 5

print(f"{dog1.name} is a {dog1.breed}, age {dog1.age}")
print(f"{dog2.name} is a {dog2.breed}, age {dog2.age}")


# ---- Example 3: A Better Approach - Using __init__ ----
# The __init__ method automatically sets attributes when an instance is created

class Cat:
    def __init__(self, name, colour, age):
        self.name = name       # 'self' refers to the instance being created
        self.colour = colour
        self.age = age

# Now creating instances is clean and consistent
cat1 = Cat("Whiskers", "Orange", 2)
cat2 = Cat("Shadow", "Black", 4)

print(f"{cat1.name} is {cat1.colour} and {cat1.age} years old")
print(f"{cat2.name} is {cat2.colour} and {cat2.age} years old")


# ---- Example 4: Adding Methods (Functions Inside a Class) ----
# Methods define what an object can DO

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm in grade {self.grade}."

    def is_graduating(self):
        return self.grade >= 12

# Create student instances
s1 = Student("Alice", 12)
s2 = Student("Bob", 10)

print(s1.introduce())               # Hi, I'm Alice and I'm in grade 12.
print(s2.introduce())               # Hi, I'm Bob and I'm in grade 10.
print(f"{s1.name} graduating? {s1.is_graduating()}")  # True
print(f"{s2.name} graduating? {s2.is_graduating()}")  # False


# ---- Example 5: The 'self' Parameter Explained ----
# 'self' is automatically passed when you call a method on an instance
# These two calls are equivalent:

print(s1.introduce())               # Python passes s1 as 'self' automatically
print(Student.introduce(s1))        # Explicitly passing s1 as 'self'

# KEY TAKEAWAYS:
# - A class is a template/blueprint for creating objects
# - An instance is a specific object created from a class
# - __init__ sets up initial attributes when an instance is created
# - 'self' refers to the current instance
# - Methods are functions defined inside a class
