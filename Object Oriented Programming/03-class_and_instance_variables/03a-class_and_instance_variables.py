#!/usr/bin/env python

# =============================================================================
# MODULE 03: CLASS VARIABLES vs INSTANCE VARIABLES (Beginner-Intermediate)
# =============================================================================
#
# GOALS:
#   1. Understand the difference between class and instance variables
#   2. Learn when to use each type
#   3. See how class variables are shared across all instances
#   4. Understand the variable lookup chain (instance -> class -> parent)
#   5. Use class variables for counters, constants, and shared data
#
# INSTANCE VARIABLES: Unique to each instance. Defined in __init__ using self.
# CLASS VARIABLES:    Shared across ALL instances. Defined directly in the class.
#
# =============================================================================

# ---- Example 1: Instance Variables (Unique Per Object) ----

class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance variable - unique per dog
        self.breed = breed    # Instance variable - unique per dog

d1 = Dog("Buddy", "Golden Retriever")
d2 = Dog("Max", "Poodle")

print(d1.name, d1.breed)   # Buddy Golden Retriever
print(d2.name, d2.breed)   # Max Poodle
# Each dog has its own name and breed


# ---- Example 2: Class Variables (Shared Across All Objects) ----

class Employee:
    # Class variables - shared by ALL instances
    company = "TechCorp"
    raise_amount = 1.04         # 4% annual raise
    num_employees = 0           # Track total employees

    def __init__(self, first, last, pay):
        # Instance variables - unique per employee
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_employees += 1     # Modify via class name!

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # Uses self to allow override

    def info(self):
        return f"{self.first} {self.last} | Pay: ${self.pay:,} | Company: {self.company}"

print(f"Employees before: {Employee.num_employees}")   # 0

e1 = Employee("Alice", "Smith", 70000)
e2 = Employee("Bob", "Jones", 80000)

print(f"Employees after: {Employee.num_employees}")     # 2
print(e1.info())
print(e2.info())


# ---- Example 3: How the Lookup Chain Works ----
# When you access an attribute, Python looks: instance -> class -> parent class

print("\n--- Namespace Exploration ---")
print(f"e1.__dict__: {e1.__dict__}")           # Only instance vars
print(f"Employee.__dict__ (partial):")
for key in ['company', 'raise_amount', 'num_employees']:
    print(f"  {key}: {Employee.__dict__[key]}")

# 'company' is NOT in e1.__dict__, but Python finds it in Employee.__dict__
print(f"\ne1.company = {e1.company}")           # Found in class
print(f"Employee.company = {Employee.company}") # Found in class (same thing)


# ---- Example 4: Overriding Class Variables on an Instance ----

print("\n--- Override Demo ---")
print(f"Before override:")
print(f"  e1.raise_amount = {e1.raise_amount}")    # 1.04 (from class)
print(f"  e2.raise_amount = {e2.raise_amount}")    # 1.04 (from class)

# Override raise_amount for e1 ONLY
e1.raise_amount = 1.10    # Creates an INSTANCE variable, doesn't change class!

print(f"\nAfter e1.raise_amount = 1.10:")
print(f"  e1.raise_amount = {e1.raise_amount}")    # 1.10 (from instance!)
print(f"  e2.raise_amount = {e2.raise_amount}")    # 1.04 (still from class)
print(f"  Employee.raise_amount = {Employee.raise_amount}")  # 1.04 (unchanged)

# Now e1 has 'raise_amount' in its own __dict__
print(f"\n  e1.__dict__: {e1.__dict__}")   # Contains raise_amount
print(f"  e2.__dict__: {e2.__dict__}")     # Does NOT contain raise_amount


# ---- Example 5: Class Variable as Counter ----

class Vehicle:
    total_vehicles = 0
    all_vehicles = []

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Vehicle.total_vehicles += 1         # Always use ClassName for counters
        Vehicle.all_vehicles.append(self)   # Track all instances

    def __repr__(self):
        return f"{self.make} {self.model}"

v1 = Vehicle("Toyota", "Camry")
v2 = Vehicle("Honda", "Civic")
v3 = Vehicle("Ford", "Mustang")

print(f"\nTotal vehicles: {Vehicle.total_vehicles}")       # 3
print(f"All vehicles: {Vehicle.all_vehicles}")             # List of all vehicles


# ---- Example 6: Class Variables as Constants ----

class Circle:
    PI = 3.14159265358979    # Class variable as a constant

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2    # Access via class name

    def circumference(self):
        return 2 * Circle.PI * self.radius

c = Circle(5)
print(f"\nCircle with radius {c.radius}")
print(f"Area: {c.area():.2f}")               # 78.54
print(f"Circumference: {c.circumference():.2f}")  # 31.42


# KEY TAKEAWAYS:
# - Instance variables (self.x) are unique to each object
# - Class variables are shared by ALL instances
# - Python lookup order: instance -> class -> parent class
# - Setting an attribute on an instance creates an instance variable
#   (it does NOT change the class variable)
# - Use ClassName.var (not self.var) to modify shared class variables
# - Common uses for class variables: counters, constants, configuration
