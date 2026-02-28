#!/usr/bin/env python

# =============================================================================
# MODULE 05: ENCAPSULATION - EXERCISES
# =============================================================================
# Test your understanding of encapsulation and access control.
# =============================================================================


# ---- Exercise 1: Identify Access Levels ----
# For each attribute, state whether it's public, protected, or private:

class Server:
    def __init__(self, hostname, ip, password):
        self.hostname = hostname        # ???
        self._ip = ip                   # ???
        self.__password = password      # ???
        self._port = 8080               # ???
        self.__max_connections = 100    # ???

# Write your answers as comments here:




# ---- Exercise 2: Create an Encapsulated Class ----
# Create a class 'StudentGrade' with:
#   - Private attribute: __grade (0-100)
#   - Getter: get_grade() returns the grade
#   - Setter: set_grade(value) validates 0 <= value <= 100
#   - Method: get_letter() returns A (90+), B (80+), C (70+), D (60+), F (<60)

# YOUR CODE HERE:




# ---- Exercise 3: Fix the Encapsulation ----
# The class below has NO encapsulation. Refactor it to:
#   - Make 'items' and 'total' private
#   - Add proper methods to add items and get the total
#   - Validate that prices are positive

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    # Currently, anyone can do: cart.total = -1000 (BAD!)
    # Currently, anyone can do: cart.items.append(("Free stuff", -999)) (BAD!)

# YOUR REFACTORED CODE HERE:




# ---- Exercise 4: Predict the Output ----

class Secret:
    def __init__(self):
        self.public = "I'm public"
        self._protected = "I'm protected"
        self.__private = "I'm private"

    def reveal(self):
        return self.__private

s = Secret()

# Prediction: ___
print(s.public)

# Prediction: ___
print(s._protected)

# Will this work? What will happen?
try:
    print(s.__private)
except AttributeError:
    print("AttributeError raised!")

# Prediction: ___
print(s.reveal())

# Prediction: ___
print(s._Secret__private)

# Prediction: What's in s.__dict__?
print(s.__dict__)


# ---- Exercise 5: Immutable Once Set ----
# Create a class 'ImmutableConfig' where:
#   - Attributes can be set ONCE in __init__ but never changed after
#   - Attempting to change raises an error
#   - Getter methods provide read access
# Hint: Use a flag like __locked

# YOUR CODE HERE:




# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: hostname=public, _ip=protected, __password=private,
#             _port=protected, __max_connections=private
#
# Exercise 2: if not (0 <= value <= 100): raise ValueError(...)
#
# Exercise 3: Make __items and __total private, add add_item() method
#             with price validation
#
# Exercise 4: public prints fine, _protected prints fine,
#             __private raises AttributeError, reveal() works,
#             _Secret__private works, __dict__ shows mangled name
#
# Exercise 5: class ImmutableConfig:
#                 def __init__(self, **kwargs):
#                     for key, val in kwargs.items():
#                         object.__setattr__(self, f'_{key}', val)
#                     object.__setattr__(self, '_locked', True)
#                 def __setattr__(self, name, value):
#                     if hasattr(self, '_locked'):
#                         raise AttributeError("Config is immutable!")
#                     super().__setattr__(name, value)
# =============================================================================
