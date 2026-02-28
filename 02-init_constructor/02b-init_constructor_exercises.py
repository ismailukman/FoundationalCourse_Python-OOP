#!/usr/bin/env python

# =============================================================================
# MODULE 02: THE __init__ CONSTRUCTOR - EXERCISES
# =============================================================================
# Test your understanding of constructors and initialisation.
# Try to solve each exercise before looking at the hints.
# =============================================================================


# ---- Exercise 1: Basic Constructor ----
# Create a class 'Circle' with:
#   - __init__ takes 'radius' as parameter
#   - Attribute: radius
#   - Computed attribute: diameter (radius * 2)
#   - Computed attribute: area (3.14159 * radius ** 2)
# Create a circle with radius 5 and print all three values.

# YOUR CODE HERE:




# ---- Exercise 2: Default Values ----
# Create a class 'Coffee' with:
#   - __init__ takes: size (default="Medium"), flavour (default="Regular"),
#     extra_shot (default=False)
#   - Method: describe() returns a description string
# Create three coffees: one with all defaults, one large vanilla,
# and one medium with extra shot.

# YOUR CODE HERE:




# ---- Exercise 3: Validation ----
# Create a class 'Password' with:
#   - __init__ takes a password string
#   - Validate: must be at least 8 characters long
#   - Validate: must contain at least one digit
#   - If invalid, raise ValueError with appropriate message
#   - Attribute: strength -> "weak" (8-10 chars), "medium" (11-15), "strong" (16+)

# YOUR CODE HERE:




# ---- Exercise 4: Mutable Default Trap ----
# What's wrong with this code? Fix it.
#
# class ShoppingCart:
#     def __init__(self, items=[]):
#         self.items = items
#
#     def add(self, item):
#         self.items.append(item)
#
# cart1 = ShoppingCart()
# cart1.add("Apple")
# cart2 = ShoppingCart()
# print(cart2.items)    # What prints? Why?

# YOUR FIX HERE:




# ---- Exercise 5: Predict the Output ----
# What will each print statement output? Write your predictions first.

class Builder:
    def __init__(self, base, multiplier=2):
        self.result = base * multiplier
        self.steps = 1

    def add(self, value):
        self.result += value
        self.steps += 1
        return self

b = Builder(5)
# Prediction for print(b.result): ___
print(b.result)

# Prediction for print(b.steps): ___
print(b.steps)

b.add(3).add(7)
# Prediction for print(b.result): ___
print(b.result)

# Prediction for print(b.steps): ___
print(b.steps)

b2 = Builder(3, 4)
# Prediction for print(b2.result): ___
print(b2.result)


# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: import math; area = math.pi * radius ** 2 (or use 3.14159)
#
# Exercise 2: def describe(self):
#                 desc = f"{self.size} {self.flavour} Coffee"
#                 if self.extra_shot: desc += " with extra shot"
#
# Exercise 3: if len(password) < 8: raise ValueError(...)
#             if not any(c.isdigit() for c in password): raise ValueError(...)
#
# Exercise 4: The list [] is shared across ALL instances. Use None as default.
#             cart2.items would print ["Apple"] because cart1 and cart2 share
#             the same list. Fix: def __init__(self, items=None):
#
# Exercise 5: b.result=10, b.steps=1, after adds: result=20, steps=3, b2=12
# =============================================================================
