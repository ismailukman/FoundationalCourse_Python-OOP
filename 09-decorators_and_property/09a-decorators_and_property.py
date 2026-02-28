#!/usr/bin/env python

# =============================================================================
# MODULE 09: DECORATORS AND PROPERTY (Advanced)
# =============================================================================
#
# GOALS:
#   1. Understand what decorators are and how they work
#   2. Create and use function decorators
#   3. Master @property for clean getter/setter syntax
#   4. Use @classmethod and @staticmethod (reviewed from Module 04)
#   5. Build custom class decorators
#   6. Understand decorator chaining and parameterised decorators
#
# A DECORATOR is a function that takes another function (or class) and
# extends its behaviour WITHOUT modifying its source code. It's a way
# to "wrap" functionality around existing functions.
#
# The @property decorator is a Pythonic way to implement getters, setters,
# and deleters — making method calls look like attribute access.
#
# =============================================================================

# ---- Example 1: How Decorators Work (Under the Hood) ----

# A decorator is just a function that takes a function and returns a function
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

# Without @ syntax (manual decoration):
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)    # This IS what @ does!
say_hello()

print("---")

# With @ syntax (syntactic sugar - same thing, cleaner):
@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()


# ---- Example 2: Decorators with Arguments ----

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("\n--- Logging Decorator ---")
add(3, 5)
greet("Alice", greeting="Hi")


# ---- Example 3: Practical Decorators ----

import time

def timer(func):
    """Measure how long a function takes to run."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done!"

print("\n--- Timer Decorator ---")
slow_function()


def retry(max_attempts=3):
    """Retry a function if it raises an exception."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def risky_operation(succeed_on=3):
    """Simulates a function that might fail."""
    import random
    if random.random() > 0.5:
        return "Success!"
    raise ConnectionError("Connection failed")


# ---- Example 4: @property - The Pythonic Way ----
# @property replaces manual getters/setters with clean attribute-like syntax

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # GETTER: access like an attribute: emp.email
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"

    # GETTER: access like an attribute: emp.fullname
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # SETTER: set like an attribute: emp.fullname = "New Name"
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # DELETER: del emp.fullname
    @fullname.deleter
    def fullname(self):
        print("Deleting name!")
        self.first = None
        self.last = None

print("\n--- @property Demo ---")
emp = Employee("John", "Smith", 50000)
print(f"Email: {emp.email}")           # Calls the getter (looks like attribute!)
print(f"Name: {emp.fullname}")         # Calls the getter

emp.fullname = "Jane Doe"              # Calls the setter!
print(f"New email: {emp.email}")       # Automatically updated!
print(f"New name: {emp.fullname}")


# ---- Example 5: @property for Validation ----

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = None
        self.celsius = celsius    # Uses the setter for validation!

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"{value}°C is below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9    # Uses celsius setter!

    def __repr__(self):
        return f"Temperature({self._celsius}°C / {self.fahrenheit}°F)"

print("\n--- @property Validation ---")
t = Temperature(100)
print(t)                        # Temperature(100°C / 212.0°F)

t.fahrenheit = 32               # Set via Fahrenheit!
print(t)                        # Temperature(0.0°C / 32.0°F)

try:
    t.celsius = -300            # Below absolute zero!
except ValueError as e:
    print(f"Caught: {e}")


# ---- Example 6: @property for Computed Attributes ----

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        """Read-only computed property."""
        return self._width * self._height

    @property
    def perimeter(self):
        """Read-only computed property."""
        return 2 * (self._width + self._height)

    @property
    def is_square(self):
        return self._width == self._height

print("\n--- Computed Properties ---")
r = Rectangle(5, 3)
print(f"Rectangle {r.width}x{r.height}")
print(f"Area: {r.area}")              # Computed on the fly
print(f"Perimeter: {r.perimeter}")    # Computed on the fly
print(f"Is square? {r.is_square}")

r.width = 3                           # Change width
print(f"After resize: {r.width}x{r.height}")
print(f"Area: {r.area}")              # Automatically recalculated!
print(f"Is square? {r.is_square}")    # Now True!


# ---- Example 7: Class Decorator ----

def add_greeting(cls):
    """A decorator that adds a greet() method to any class."""
    def greet(self):
        return f"Hello, I'm a {cls.__name__}!"
    cls.greet = greet
    return cls

@add_greeting
class Robot:
    def __init__(self, name):
        self.name = name

print("\n--- Class Decorator ---")
r = Robot("R2D2")
print(r.greet())    # Hello, I'm a Robot!


# KEY TAKEAWAYS:
# - Decorators wrap functions to extend behaviour without modifying them
# - @decorator is syntax sugar for: func = decorator(func)
# - Use *args, **kwargs in wrapper to handle any function signature
# - @property creates getter/setter/deleter with attribute-like syntax
# - @property is Pythonic way to replace manual get_x()/set_x() methods
# - Computed properties (@property with no setter) are read-only
# - Use property setters for validation and side effects
# - Class decorators can add methods or modify entire classes
