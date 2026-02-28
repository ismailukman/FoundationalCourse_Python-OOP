#!/usr/bin/env python

# =============================================================================
# MODULE 10: ABSTRACT CLASSES AND ADVANCED OOP (Very Advanced)
# =============================================================================
#
# GOALS:
#   1. Understand Abstract Base Classes (ABC) and abstract methods
#   2. Use the abc module to enforce class contracts
#   3. Master multiple inheritance and Method Resolution Order (MRO)
#   4. Learn Mixins — small reusable classes for shared behaviour
#   5. Explore common OOP design patterns (Singleton, Factory, Observer)
#   6. Understand composition vs inheritance
#
# ABSTRACT CLASSES are classes that CANNOT be instantiated directly.
# They define a "contract" (interface) that subclasses MUST follow.
# This is how you enforce structure across a class hierarchy.
#
# =============================================================================

from abc import ABC, abstractmethod


# ---- Example 1: Abstract Base Classes (ABC) ----

class Shape(ABC):
    """Abstract class - defines WHAT subclasses must do, not HOW."""

    @abstractmethod
    def area(self):
        """Every shape MUST implement area()."""
        pass

    @abstractmethod
    def perimeter(self):
        """Every shape MUST implement perimeter()."""
        pass

    def describe(self):
        """Concrete method - shared by ALL shapes (can be used directly)."""
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


print("--- Abstract Base Classes ---")

# shape = Shape()    # TypeError: Can't instantiate abstract class!

c = Circle(5)
s = Square(4)
print(c.describe())    # Circle: area=78.54, perimeter=31.42
print(s.describe())    # Square: area=16.00, perimeter=16.00

# We can treat them the same thanks to the abstract contract:
shapes = [Circle(3), Square(5), Circle(7)]
total_area = sum(shape.area() for shape in shapes)
print(f"Total area: {total_area:.2f}")


# ---- Example 2: Abstract Properties ----

class Vehicle(ABC):
    @property
    @abstractmethod
    def max_speed(self):
        pass

    @property
    @abstractmethod
    def fuel_type(self):
        pass

    def info(self):
        return f"{self.__class__.__name__}: max {self.max_speed} km/h, fuel: {self.fuel_type}"


class Car(Vehicle):
    @property
    def max_speed(self):
        return 200

    @property
    def fuel_type(self):
        return "Petrol"


class Bicycle(Vehicle):
    @property
    def max_speed(self):
        return 40

    @property
    def fuel_type(self):
        return "Human power"

print("\n--- Abstract Properties ---")
print(Car().info())
print(Bicycle().info())


# ---- Example 3: Multiple Inheritance ----
# Python supports inheriting from MULTIPLE parent classes.

class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} is flying!"

class Swimmable:
    def swim(self):
        return f"{self.__class__.__name__} is swimming!"

class Walkable:
    def walk(self):
        return f"{self.__class__.__name__} is walking!"

# Duck inherits from ALL three:
class Duck(Flyable, Swimmable, Walkable):
    pass

# Penguin can swim and walk but NOT fly:
class Penguin(Swimmable, Walkable):
    pass

print("\n--- Multiple Inheritance ---")
d = Duck()
print(d.fly())       # Duck is flying!
print(d.swim())      # Duck is swimming!
print(d.walk())      # Duck is walking!

p = Penguin()
print(p.swim())      # Penguin is swimming!
print(p.walk())      # Penguin is walking!


# ---- Example 4: Method Resolution Order (MRO) ----
# When multiple parents define the same method, Python follows the MRO
# to decide which one to call. It uses the C3 Linearisation algorithm.

class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):
    pass        # Does NOT define who() — which parent's version?

print("\n--- Method Resolution Order (MRO) ---")
d = D()
print(f"D().who() = {d.who()}")    # "B" — B comes first in D(B, C)

print(f"\nMRO for D: {[cls.__name__ for cls in D.__mro__]}")
# => ['D', 'B', 'C', 'A', 'object']
# Python checks: D -> B -> C -> A -> object


# ---- Example 5: Mixins — Small Reusable Classes ----
# Mixins are NOT standalone — they add specific behaviour to other classes.

class SerializableMixin:
    """Adds JSON serialisation capability."""
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    def to_json(self):
        import json
        return json.dumps(self.to_dict(), indent=2, default=str)


class PrintableMixin:
    """Adds a formatted print method."""
    def print_info(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items()
                         if not k.startswith('_'))
        print(f"[{self.__class__.__name__}] {attrs}")


class Student(SerializableMixin, PrintableMixin):
    def __init__(self, name, grade, gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa


print("\n--- Mixins ---")
s = Student("Alice", "A", 3.9)
s.print_info()             # [Student] name=Alice, grade=A, gpa=3.9
print(s.to_json())         # JSON representation


# ---- Example 6: Composition vs Inheritance ----
# "Favour composition over inheritance" — don't always use IS-A.
# Sometimes HAS-A is a better model.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine ({self.horsepower}hp) started!"


class GPS:
    def navigate(self, destination):
        return f"Navigating to {destination}..."


class MusicPlayer:
    def play(self, song):
        return f"♪ Playing: {song}"


# Car HAS-A engine, GPS, and music player — NOT IS-A
class SmartCar:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)      # Composition!
        self.gps = GPS()                      # Composition!
        self.music = MusicPlayer()            # Composition!

    def start(self):
        return f"{self.brand}: {self.engine.start()}"

print("\n--- Composition over Inheritance ---")
car = SmartCar("Tesla", 450)
print(car.start())                       # Tesla: Engine (450hp) started!
print(car.gps.navigate("Paris"))         # Navigating to Paris...
print(car.music.play("Imagine"))         # ♪ Playing: Imagine


# ---- Example 7: Singleton Pattern ----
# Ensures only ONE instance of a class ever exists.

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Database(Singleton):
    def __init__(self, name="default"):
        if not hasattr(self, 'initialized'):
            self.name = name
            self.initialized = True
            print(f"Database '{name}' created")

print("\n--- Singleton Pattern ---")
db1 = Database("production")     # Database 'production' created
db2 = Database("testing")        # No output — same instance!
print(f"db1 is db2: {db1 is db2}")    # True
print(f"db1.name: {db1.name}")        # production (not overwritten)


# ---- Example 8: Factory Pattern ----
# A factory method creates objects without specifying the exact class.

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Fish(Animal):
    def speak(self):
        return "..."

class AnimalFactory:
    """Creates the right Animal subclass based on a string."""
    _animals = {
        "dog": Dog,
        "cat": Cat,
        "fish": Fish
    }

    @classmethod
    def create(cls, animal_type):
        animal_class = cls._animals.get(animal_type.lower())
        if animal_class is None:
            raise ValueError(f"Unknown animal: {animal_type}")
        return animal_class()

print("\n--- Factory Pattern ---")
for kind in ["dog", "cat", "fish"]:
    animal = AnimalFactory.create(kind)
    print(f"{kind}: {animal.speak()}")


# ---- Example 9: Observer Pattern ----
# Objects (observers) subscribe to events from a subject.

class EventEmitter:
    """Subject that emits events to registered observers."""
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        """Register a listener for an event."""
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    def emit(self, event, *args, **kwargs):
        """Notify all listeners of an event."""
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)


class Store(EventEmitter):
    def __init__(self):
        super().__init__()
        self._items = {}

    def add_item(self, name, price):
        self._items[name] = price
        self.emit("item_added", name, price)

    def remove_item(self, name):
        if name in self._items:
            del self._items[name]
            self.emit("item_removed", name)


print("\n--- Observer Pattern ---")
store = Store()

# Register observers:
store.on("item_added", lambda name, price: print(f"  [LOG] Added '{name}' at ${price}"))
store.on("item_added", lambda name, price: print(f"  [EMAIL] New item notification: {name}"))
store.on("item_removed", lambda name: print(f"  [LOG] Removed '{name}'"))

store.add_item("Laptop", 999)
store.add_item("Mouse", 29)
store.remove_item("Mouse")


# KEY TAKEAWAYS:
# - Abstract classes (ABC) define contracts that subclasses MUST implement
# - You CANNOT instantiate an abstract class directly
# - Multiple inheritance lets a class inherit from many parents
# - MRO (Method Resolution Order) determines which method gets called
# - Mixins are small reusable classes that add specific behaviour
# - Composition (HAS-A) is often better than inheritance (IS-A)
# - Design patterns (Singleton, Factory, Observer) are reusable OOP solutions
# - Python's abc module provides ABC and @abstractmethod
