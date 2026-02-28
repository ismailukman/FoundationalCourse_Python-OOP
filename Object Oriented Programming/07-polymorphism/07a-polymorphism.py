#!/usr/bin/env python

# =============================================================================
# MODULE 07: POLYMORPHISM (Intermediate-Advanced)
# =============================================================================
#
# GOALS:
#   1. Understand polymorphism - "many forms" in OOP
#   2. Learn method overriding as a form of polymorphism
#   3. Understand duck typing in Python
#   4. Use polymorphism with common interfaces
#   5. Apply operator overloading (basic intro, more in Module 08)
#
# POLYMORPHISM means "many forms". In OOP, it allows objects of different
# classes to be treated through the same interface. The same method name
# can behave differently depending on the object type.
#
# Python uses DUCK TYPING: "If it walks like a duck and quacks like a duck,
# then it's a duck." - We care about WHAT an object can do, not WHAT it is.
#
# =============================================================================

# ---- Example 1: Method Overriding (Runtime Polymorphism) ----
# Different classes implement the same method differently

class Shape:
    def area(self):
        return 0

    def describe(self):
        return "I am a shape"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def describe(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        return f"Rectangle {self.width}x{self.height}"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def describe(self):
        return f"Triangle base={self.base}, height={self.height}"

# POLYMORPHISM: Same interface (area(), describe()), different behaviour
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

print("--- Shape Areas (Polymorphism) ---")
for shape in shapes:
    print(f"{shape.describe()} -> Area: {shape.area():.2f}")


# ---- Example 2: Duck Typing ----
# Python doesn't require inheritance to use polymorphism!
# Any object with the right methods works.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop!"

# These classes have NO common parent, but they all have speak()
def make_it_speak(thing):
    """Works with ANY object that has a speak() method."""
    print(thing.speak())

print("\n--- Duck Typing ---")
make_it_speak(Dog())      # Woof!
make_it_speak(Cat())      # Meow!
make_it_speak(Robot())    # Beep boop!
# Python doesn't care about the TYPE, only that it HAS the method!


# ---- Example 3: Polymorphism with Built-in Functions ----
# Python's built-in functions use polymorphism extensively

print("\n--- Built-in Polymorphism ---")
# len() works on strings, lists, dicts, tuples - different types, same function
print(len("Hello"))       # 5 (string)
print(len([1, 2, 3]))    # 3 (list)
print(len({"a": 1}))     # 1 (dict)

# + operator works differently for different types
print(3 + 4)              # 7 (integer addition)
print("Hello" + " World") # Hello World (string concatenation)
print([1, 2] + [3, 4])   # [1, 2, 3, 4] (list concatenation)

# iter() works on any iterable
for char in "Hi":
    print(char, end=" ")
print()


# ---- Example 4: Polymorphism with Common Interface ----
# Design classes that share a common interface for interchangeable use

class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")

    def refund(self, amount):
        raise NotImplementedError("Subclasses must implement refund()")

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Paid ${amount:.2f} with Credit Card ending in {self.card_number[-4:]}"

    def refund(self, amount):
        return f"Refunded ${amount:.2f} to Credit Card ending in {self.card_number[-4:]}"

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid ${amount:.2f} via PayPal ({self.email})"

    def refund(self, amount):
        return f"Refunded ${amount:.2f} to PayPal ({self.email})"

class Bitcoin(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet = wallet_address

    def pay(self, amount):
        return f"Paid ${amount:.2f} in Bitcoin to wallet {self.wallet[:8]}..."

    def refund(self, amount):
        return f"Refunded ${amount:.2f} in Bitcoin to wallet {self.wallet[:8]}..."

# Process ANY payment method the same way - polymorphism!
def process_payment(method, amount):
    print(method.pay(amount))

print("\n--- Payment Processing ---")
methods = [
    CreditCard("4532123456789012"),
    PayPal("user@email.com"),
    Bitcoin("1A2b3C4d5E6f7G8h")
]

for method in methods:
    process_payment(method, 99.99)


# ---- Example 5: Polymorphism with Operator Overloading ----

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print("\n--- Operator Overloading ---")
v1 = Vector(2, 3)
v2 = Vector(4, 1)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")      # Uses __add__
print(f"v1 * 3 = {v1 * 3}")        # Uses __mul__
print(f"v1 == v2? {v1 == v2}")      # Uses __eq__
print(f"v1 == Vector(2,3)? {v1 == Vector(2, 3)}")  # True


# ---- Example 6: Polymorphic Iteration ----

class FileReader:
    def read(self):
        return "Reading from file..."

class DatabaseReader:
    def read(self):
        return "Reading from database..."

class APIReader:
    def read(self):
        return "Reading from API..."

# All readers used interchangeably
def load_data(readers):
    for reader in readers:
        print(reader.read())

print("\n--- Polymorphic Data Loading ---")
readers = [FileReader(), DatabaseReader(), APIReader()]
load_data(readers)


# KEY TAKEAWAYS:
# - Polymorphism = same interface, different implementations
# - Method overriding: child classes redefine parent methods
# - Duck typing: Python cares about BEHAVIOUR, not TYPE
# - Built-in functions (len, +, iter) are polymorphic by design
# - Operator overloading: define how operators work with your classes
# - Design classes with COMMON INTERFACES for maximum flexibility
# - "Program to an interface, not an implementation"
