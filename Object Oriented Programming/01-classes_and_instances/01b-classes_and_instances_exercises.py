#!/usr/bin/env python

# =============================================================================
# MODULE 01: CLASSES AND INSTANCES - EXERCISES
# =============================================================================
# Test your understanding of classes and instances.
# Try to solve each exercise before looking at the hints.
# =============================================================================


# ---- Exercise 1: Create a Simple Class ----
# Create a class called 'Book' with the following attributes:
#   - title (string)
#   - author (string)
#   - pages (integer)
# Then create two Book instances and print their details.

# YOUR CODE HERE:




# ---- Exercise 2: Add a Method ----
# Add a method called 'description()' to the Book class that returns
# a string like: "Title by Author, Pages pages"
# Example: "Python Basics by John Smith, 250 pages"

# YOUR CODE HERE:




# ---- Exercise 3: Create a Rectangle Class ----
# Create a class called 'Rectangle' with:
#   - Attributes: width, height
#   - Method: area() -> returns width * height
#   - Method: perimeter() -> returns 2 * (width + height)
# Create a rectangle with width=5, height=3 and print its area and perimeter.

# YOUR CODE HERE:




# ---- Exercise 4: Class with Default Values ----
# Create a class called 'Counter' with:
#   - An attribute 'count' that starts at 0 (default value)
#   - A method 'increment()' that increases count by 1
#   - A method 'decrement()' that decreases count by 1
#   - A method 'get_count()' that returns the current count
# Hint: def __init__(self, count=0):

# YOUR CODE HERE:




# ---- Exercise 5: Understanding 'self' ----
# Given the class below, predict what each print statement will output.
# Write your predictions as comments, then run the code to verify.

class Mystery:
    def __init__(self, x):
        self.value = x * 2

    def add(self, y):
        self.value += y
        return self.value

m = Mystery(5)
# Prediction for print(m.value): ___
print(m.value)

# Prediction for print(m.add(3)): ___
print(m.add(3))

# Prediction for print(m.value): ___
print(m.value)

# Prediction for print(m.add(7)): ___
print(m.add(7))


# =============================================================================
# HINTS (try solving first!)
# =============================================================================
# Exercise 1: class Book:
#                 def __init__(self, title, author, pages):
#
# Exercise 2: def description(self):
#                 return f"{self.title} by {self.author}, {self.pages} pages"
#
# Exercise 3: def area(self):
#                 return self.width * self.height
#
# Exercise 4: Use a default parameter: def __init__(self, count=0)
#
# Exercise 5: m.value starts at 5*2=10, add(3) -> 10+3=13, etc.
# =============================================================================
