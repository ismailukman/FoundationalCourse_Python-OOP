#!/usr/bin/env python

# =============================================================================
# MODULE 06: INHERITANCE (Intermediate)
# =============================================================================
#
# GOALS:
#   1. Understand what inheritance is and why it's useful
#   2. Create parent (base) and child (derived) classes
#   3. Use super() to call parent class methods
#   4. Override methods in child classes
#   5. Understand the isinstance() and issubclass() functions
#   6. Learn method resolution order (MRO)
#
# INHERITANCE allows a class to inherit attributes and methods from another
# class. This promotes code reuse and establishes a natural hierarchy.
#
# TERMINOLOGY:
#   - Parent / Base / Super class: the class being inherited FROM
#   - Child / Derived / Sub class: the class that inherits
#
# =============================================================================

# ---- Example 1: Basic Inheritance ----

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound"

    def info(self):
        return f"{self.name} is a {self.species}"

# Dog inherits from Animal - gets ALL of Animal's methods and attributes
class Dog(Animal):
    pass

# Cat also inherits from Animal
class Cat(Animal):
    pass

d = Dog("Buddy", "Canine")
c = Cat("Whiskers", "Feline")

print(d.info())         # Buddy is a Canine (inherited from Animal)
print(c.info())         # Whiskers is a Feline (inherited from Animal)
print(d.speak())        # Buddy makes a sound
print(c.speak())        # Whiskers makes a sound


print("\n---")

# ---- Example 2: Overriding Methods ----
# Child classes can OVERRIDE parent methods to provide specific behaviour

class Animal2:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog2(Animal2):
    def speak(self):                          # Overrides Animal2.speak()
        return f"{self.name} says Woof!"

class Cat2(Animal2):
    def speak(self):                          # Overrides Animal2.speak()
        return f"{self.name} says Meow!"

class Duck(Animal2):
    def speak(self):
        return f"{self.name} says Quack!"

print("\n--- Method Overriding ---")
animals = [Dog2("Rex"), Cat2("Luna"), Duck("Donald")]
for animal in animals:
    print(animal.speak())    # Each calls its OWN version of speak()


print("\n---")
# ---- Example 3: Extending the Parent with super() ----
# super() lets you call the PARENT class's methods from the child

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"{self.fullname()} | ${self.pay:,}"

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Call parent's __init__
        self.prog_lang = prog_lang          # Add new attribute

    def __repr__(self):
        return f"{self.fullname()} | ${self.pay:,} | Lang: {self.prog_lang}"

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees if employees is not None else []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_team(self):
        print(f"\n{self.fullname()}'s team:")
        for emp in self.employees:
            print(f"  → {emp.fullname()}")

print("\n--- Employee Hierarchy ---")
dev1 = Developer("Alice", "Smith", 90000, "Python")
dev2 = Developer("Bob", "Jones", 85000, "JavaScript")
mgr = Manager("Carol", "White", 110000)

print(dev1)
print(dev2)
mgr.add_employee(dev1)
mgr.add_employee(dev2)
mgr.show_team()


print("\n---")
# ---- Example 4: isinstance() and issubclass() ----

print("\n--- Type Checking ---")
print(f"dev1 is Employee? {isinstance(dev1, Employee)}")      # True
print(f"dev1 is Developer? {isinstance(dev1, Developer)}")    # True
print(f"dev1 is Manager? {isinstance(dev1, Manager)}")        # False

print(f"Developer subclass of Employee? {issubclass(Developer, Employee)}")  # True
print(f"Manager subclass of Employee? {issubclass(Manager, Employee)}")      # True
print(f"Developer subclass of Manager? {issubclass(Developer, Manager)}")    # False


# ---- Example 5: Multi-Level Inheritance ----
# A -> B -> C (chain of inheritance)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors=4):
        super().__init__(make, model, year)
        self.doors = doors

    def description(self):
        return f"{super().description()} ({self.doors}-door)"

class ElectricCar(Car):
    def __init__(self, make, model, year, doors=4, battery_kwh=75):
        super().__init__(make, model, year, doors)
        self.battery_kwh = battery_kwh

    def description(self):
        return f"{super().description()} | Battery: {self.battery_kwh} kWh"

print("\n--- Multi-Level Inheritance ---")
v = Vehicle("Toyota", "Camry", 2024)
c = Car("Honda", "Civic", 2024, 4)
e = ElectricCar("Tesla", "Model 3", 2024, 4, 82)

print(v.description())   # 2024 Toyota Camry
print(c.description())   # 2024 Honda Civic (4-door)
print(e.description())   # 2024 Tesla Model 3 (4-door) | Battery: 82 kWh

# Method Resolution Order (MRO) - the order Python searches for methods
print(f"\nMRO for ElectricCar:")
for cls in ElectricCar.__mro__:
    print(f"  {cls.__name__}")

print("\n---")

# ---- Example 6: Using Parent Methods Alongside Overridden Ones ----

class Shape:
    def __init__(self, colour="black"):
        self.colour = colour

    def describe(self):
        return f"A {self.colour} shape"

class Circle(Shape):
    def __init__(self, radius, colour="black"):
        super().__init__(colour)
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def describe(self):
        # Call parent's describe() and ADD to it
        base = super().describe()
        return f"{base} (circle, radius={self.radius}, area={self.area():.2f})"

print("\n--- Extending Parent Methods ---")
s = Shape("red")
print(s.describe())      # A red shape

c = Circle(5, "blue")
print(c.describe())      # A blue shape (circle, radius=5, area=78.54)


# KEY TAKEAWAYS:
# - Inheritance lets child classes reuse parent class code
# - Child classes can OVERRIDE parent methods for specific behaviour
# - Use super() to call parent class methods from the child
# - super().__init__() is essential to initialise parent attributes
# - isinstance() checks if an object is an instance of a class (or its parents)
# - issubclass() checks if a class is derived from another
# - MRO determines the order methods are searched: child → parent → grandparent
