#!/usr/bin/env python

# =============================================================================
# MODULE 06: INHERITANCE - EXERCISES
# =============================================================================
# Test your understanding of inheritance, super(), and method overriding.
# =============================================================================


# ---- Exercise 1: Basic Inheritance ----
# Given the parent class below, create two child classes:
#   - 'Smartphone' with extra attribute: os (e.g., "iOS", "Android")
#   - 'Laptop' with extra attribute: ram_gb
# Both should call super().__init__() and override display_info()

class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"{self.brand} {self.model} - ${self.price}"

# YOUR CODE HERE:




# ---- Exercise 2: Method Override ----
# Create a class hierarchy for shapes:
#   - Parent: Shape with method area() returning 0
#   - Child: Square(side) overrides area() -> side * side
#   - Child: Triangle(base, height) overrides area() -> 0.5 * base * height
# Create instances and print their areas.

# YOUR CODE HERE:




# ---- Exercise 3: Predict the Output ----

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    pass

class D(B):
    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} and D"

a = A()
b = B()
c = C()
d = D()

# Prediction: ___
print(a.greet())

# Prediction: ___
print(b.greet())

# Prediction: ___
print(c.greet())

# Prediction: ___
print(d.greet())

# Prediction: ___
print(isinstance(d, A))

# Prediction: ___
print(isinstance(c, B))


# ---- Exercise 4: Extend Don't Replace ----
# The child class below REPLACES the parent's __init__ instead of extending.
# Fix it using super() so that parent attributes are preserved.

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        # BUG: This doesn't call parent __init__!
        self.interest_rate = interest_rate
        # After fix, self.owner and self.balance should work

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

# YOUR FIX HERE:
# Uncomment to test:
# sa = SavingsAccount("Alice", 1000, 0.05)
# print(f"{sa.owner}: ${sa.balance}")    # Should not error
# sa.add_interest()
# print(f"After interest: ${sa.balance}")


# ---- Exercise 5: Multi-Level Chain ----
# Create a 3-level inheritance chain:
#   - LivingThing: name, is_alive=True
#   - Plant(LivingThing): species, needs_sun=True
#   - Flower(Plant): colour, bloom_season
# Each level should call super().__init__() and add a describe() method
# that builds on the parent's describe().

# YOUR CODE HERE:




# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: class Smartphone(Device):
#                 def __init__(self, brand, model, price, os):
#                     super().__init__(brand, model, price)
#                     self.os = os
#
# Exercise 2: class Square(Shape):
#                 def __init__(self, side):
#                     self.side = side
#                 def area(self):
#                     return self.side * self.side
#
# Exercise 3: a="Hello from A", b="Hello from B", c="Hello from A" (inherited),
#             d="Hello from B and D", isinstance(d,A)=True, isinstance(c,B)=False
#
# Exercise 4: Add super().__init__(owner, balance) as first line in
#             SavingsAccount.__init__
#
# Exercise 5: Each describe() should call super().describe() and append info
# =============================================================================
