#!/usr/bin/env python

# =============================================================================
# MODULE 10: ABSTRACT CLASSES AND DESIGN PATTERNS - EXERCISES
# =============================================================================
# Test your understanding of abstract classes, MRO, mixins, composition,
# and design patterns.
# =============================================================================


# ---- Exercise 1: Create an Abstract Interface ----
# Create an abstract class 'PaymentProcessor' with:
#   - Abstract method: process_payment(amount) -> bool
#   - Abstract method: refund(amount) -> bool
#   - Abstract property: name
#   - Concrete method: log(message) that prints "[ProcessorName] message"
#
# Then create two concrete subclasses:
#   - CreditCardProcessor (always succeeds)
#   - PayPalProcessor (fails if amount > 1000)
# Test both and try to instantiate the abstract class (it should fail).

# YOUR CODE HERE:




# ---- Exercise 2: Predict the MRO ----
# WITHOUT running the code, predict the MRO for class F.

class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B"

class C(A):
    pass

class D(B):
    pass

class E(C):
    def greet(self):
        return "E"

class F(D, E):
    pass

# 1. What is F.__mro__?
# Prediction: ___

# 2. What does F().greet() return?
# Prediction: ___

# Reveal:
print("MRO:", [cls.__name__ for cls in F.__mro__])
print("F().greet():", F().greet())


# ---- Exercise 3: Design a Mixin System ----
# Create these mixins:
#   - TimestampMixin: adds created_at and updated_at attributes
#   - ValidatableMixin: adds validate() method that checks required_fields
#   - ComparableMixin: adds comparison based on a compare_key property
#
# Then create a class 'Product' that uses all three mixins with:
#   - Attributes: name, price, category
#   - required_fields = ['name', 'price']
#   - compare_key = price
# Test all mixin functionality.

# YOUR CODE HERE:




# ---- Exercise 4: Composition Challenge ----
# Build a Computer class using COMPOSITION (not inheritance):
#   - CPU class: brand, cores, speed_ghz; method: process(task)
#   - RAM class: size_gb; method: load(program)
#   - Storage class: size_gb, type (SSD/HDD); method: save(file)
#   - Computer: name, has CPU, RAM, Storage; method: run(program)
#
# The Computer.run() method should use all three components.

# YOUR CODE HERE:




# ---- Exercise 5: Implement a Design Pattern ----
# Implement the STRATEGY pattern:
# Create a 'TextFormatter' that can use different formatting strategies:
#   - UpperCaseStrategy: converts text to uppercase
#   - LowerCaseStrategy: converts text to lowercase
#   - TitleCaseStrategy: converts text to title case
#   - SnakeCaseStrategy: converts "Hello World" to "hello_world"
#
# Use an abstract class for the strategy interface.
# The formatter should be able to switch strategies at runtime.

# YOUR CODE HERE:




# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: from abc import ABC, abstractmethod
#             class PaymentProcessor(ABC):
#                 @abstractmethod
#                 def process_payment(self, amount): pass
#
# Exercise 2: C3 linearisation: F -> D -> B -> E -> C -> A -> object
#             F().greet() returns "B"  (D has no greet, so goes to B)
#
# Exercise 3: class TimestampMixin:
#                 def __init_subclass__(cls, **kwargs): ...
#             Or use __init__ with super() chain
#             from datetime import datetime
#
# Exercise 4: class Computer:
#                 def __init__(self, name, cpu, ram, storage):
#                     self.cpu = cpu  # HAS-A relationship
#
# Exercise 5: class FormattingStrategy(ABC):
#                 @abstractmethod
#                 def format(self, text): pass
#             class TextFormatter:
#                 def __init__(self, strategy):
#                     self.strategy = strategy
#                 def format(self, text):
#                     return self.strategy.format(text)
# =============================================================================
