#!/usr/bin/env python

# =============================================================================
# MODULE 07: POLYMORPHISM - EXERCISES
# =============================================================================
# Test your understanding of polymorphism and duck typing.
# =============================================================================


# ---- Exercise 1: Method Overriding ----
# Create a class hierarchy:
#   - Animal with method make_sound() returning "..."
#   - Dog, Cat, Cow each overriding make_sound()
# Write a function animal_chorus(animals) that calls make_sound() on each.

# YOUR CODE HERE:




# ---- Exercise 2: Duck Typing ----
# Create three UNRELATED classes (no inheritance):
#   - Printer with method output(text)
#   - Speaker with method output(text)
#   - Logger with method output(text)
# Write a function broadcast(devices, message) that calls output() on each.

# YOUR CODE HERE:




# ---- Exercise 3: Predict the Output ----

class Base:
    def action(self):
        return "Base action"

    def process(self):
        return f"Processing: {self.action()}"

class ChildA(Base):
    def action(self):
        return "ChildA action"

class ChildB(Base):
    pass

class ChildC(ChildA):
    def action(self):
        return f"ChildC + {super().action()}"

# Prediction: ___
print(Base().process())

# Prediction: ___
print(ChildA().process())

# Prediction: ___
print(ChildB().process())

# Prediction: ___
print(ChildC().process())

# Prediction: ___
print(ChildC().action())


# ---- Exercise 4: Polymorphic Calculator ----
# Create classes that overload math operators:
#   - Fraction with __add__, __mul__, __eq__, __repr__
#   - Fraction(1, 2) + Fraction(1, 3) should work
# Hint: a/b + c/d = (a*d + b*c) / (b*d)

# YOUR CODE HERE:




# ---- Exercise 5: Common Interface Challenge ----
# Create a notification system where different channels
# (Email, SMS, PushNotification) all have:
#   - send(recipient, message)
#   - format_message(message)
# Write a function notify_all(channels, recipient, message).

# YOUR CODE HERE:




# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: def animal_chorus(animals):
#                 for a in animals:
#                     print(a.make_sound())
#
# Exercise 2: No inheritance needed! Just implement the same method name.
#
# Exercise 3: process() calls self.action() - which version depends on
#             the ACTUAL type of the object (polymorphism!)
#             Base:"Processing: Base action", ChildA:"Processing: ChildA action",
#             ChildB:"Processing: Base action", ChildC:"Processing: ChildC + ChildA action"
#
# Exercise 4: class Fraction:
#                 def __add__(self, other):
#                     new_num = self.num * other.den + self.den * other.num
#                     new_den = self.den * other.den
#                     return Fraction(new_num, new_den)
#
# Exercise 5: Each channel class implements send() differently but with
#             the same signature. notify_all loops and calls send() on each.
# =============================================================================
