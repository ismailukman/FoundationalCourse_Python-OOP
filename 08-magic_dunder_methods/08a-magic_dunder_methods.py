#!/usr/bin/env python

# =============================================================================
# MODULE 08: SPECIAL (MAGIC / DUNDER) METHODS (Advanced)
# =============================================================================
#
# GOALS:
#   1. Understand what magic/dunder methods are
#   2. Master __str__ and __repr__ for string representation
#   3. Implement arithmetic operators (__add__, __sub__, __mul__, etc.)
#   4. Implement comparison operators (__eq__, __lt__, __gt__, etc.)
#   5. Implement container methods (__len__, __getitem__, __contains__)
#   6. Use __call__ to make objects callable
#
# MAGIC METHODS (also called "dunder" methods for "double underscore")
# are special methods that Python calls behind the scenes. They let you
# define how your objects interact with built-in Python operations like
# +, -, ==, len(), str(), print(), [], in, etc.
#
# When you write: a + b
# Python actually calls: a.__add__(b)
#
# =============================================================================

# ---- Example 1: __str__ vs __repr__ ----
# __repr__: unambiguous, for developers (used in debugger, repr())
# __str__:  readable, for end users (used in print(), str())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"    # Unambiguous, eval()-friendly

    def __str__(self):
        return f"({self.x}, {self.y})"          # User-friendly

p = Point(3, 4)
print(repr(p))    # Point(3, 4)     <- calls __repr__
print(str(p))     # (3, 4)          <- calls __str__
print(p)          # (3, 4)          <- print() uses __str__ first
print(f"The point is {p}")  # (3, 4) <- f-strings use __str__

# In a list, __repr__ is used:
points = [Point(1, 2), Point(3, 4)]
print(points)     # [Point(1, 2), Point(3, 4)]  <- uses __repr__


# ---- Example 2: Arithmetic Operators ----

class Money:
    def __init__(self, dollars, cents=0):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @property
    def cents(self):
        return self.total_cents % 100

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(0, self.total_cents + other.total_cents)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(0, self.total_cents - other.total_cents)
        return NotImplemented

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Money(0, int(self.total_cents * factor))
        return NotImplemented

    def __repr__(self):
        return f"Money({self.dollars}, {self.cents})"

    def __str__(self):
        return f"${self.dollars}.{self.cents:02d}"

print("\n--- Arithmetic Operators ---")
m1 = Money(10, 50)      # $10.50
m2 = Money(5, 75)       # $5.75
print(f"{m1} + {m2} = {m1 + m2}")       # $10.50 + $5.75 = $16.25
print(f"{m1} - {m2} = {m1 - m2}")       # $10.50 - $5.75 = $4.75
print(f"{m1} * 3 = {m1 * 3}")           # $10.50 * 3 = $31.50


# ---- Example 3: Comparison Operators ----

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __le__(self, other):
        return self.gpa <= other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __ge__(self, other):
        return self.gpa >= other.gpa

    def __repr__(self):
        return f"Student({self.name}, GPA={self.gpa})"

print("\n--- Comparison Operators ---")
s1 = Student("Alice", 3.9)
s2 = Student("Bob", 3.5)
s3 = Student("Carol", 3.9)

print(f"{s1} == {s3}? {s1 == s3}")    # True (same GPA)
print(f"{s1} > {s2}? {s1 > s2}")      # True
print(f"{s2} < {s1}? {s2 < s1}")      # True

# Because we implemented __lt__, sorted() works!
students = [s1, s2, s3]
print(f"Sorted: {sorted(students)}")


# ---- Example 4: Container Methods ----

class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self._songs = songs if songs is not None else []

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __setitem__(self, index, value):
        self._songs[index] = value

    def __contains__(self, song):
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)

    def __repr__(self):
        return f"Playlist('{self.name}', {len(self)} songs)"

    def add(self, song):
        self._songs.append(song)

print("\n--- Container Methods ---")
pl = Playlist("Rock Classics")
pl.add("Bohemian Rhapsody")
pl.add("Stairway to Heaven")
pl.add("Hotel California")

print(f"Length: {len(pl)}")                    # __len__
print(f"First song: {pl[0]}")                  # __getitem__
print(f"Last song: {pl[-1]}")                  # __getitem__
print(f"Contains 'Hotel California'? {'Hotel California' in pl}")  # __contains__

# Can iterate because of __iter__
print("All songs:")
for song in pl:
    print(f"  ♪ {song}")

# Slicing works too!
print(f"First 2: {pl[:2]}")


# ---- Example 5: __call__ - Making Objects Callable ----

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print("\n--- Callable Objects ---")
print(f"double(5) = {double(5)}")      # 10 - calling object like a function!
print(f"triple(5) = {triple(5)}")      # 15
print(f"Is double callable? {callable(double)}")  # True

# Practical use: a flexible greeting function
class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting
        self.count = 0

    def __call__(self, name):
        self.count += 1
        return f"{self.greeting}, {name}! (Call #{self.count})"

greet = Greeter("Welcome")
print(greet("Alice"))     # Welcome, Alice! (Call #1)
print(greet("Bob"))       # Welcome, Bob! (Call #2)


# ---- Example 6: Complete Example - Custom Vector Class ----

class Vector:
    def __init__(self, *components):
        self._data = list(components)

    # String representations
    def __repr__(self):
        return f"Vector({', '.join(str(c) for c in self._data)})"

    def __str__(self):
        return f"<{', '.join(str(c) for c in self._data)}>"

    # Arithmetic
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be same length")
        return Vector(*(a + b for a, b in zip(self._data, other._data)))

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be same length")
        return Vector(*(a - b for a, b in zip(self._data, other._data)))

    def __mul__(self, scalar):
        return Vector(*(c * scalar for c in self._data))

    # Comparison
    def __eq__(self, other):
        return self._data == other._data

    # Container
    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    # Boolean
    def __bool__(self):
        return any(c != 0 for c in self._data)

    # Absolute value (magnitude)
    def __abs__(self):
        return sum(c ** 2 for c in self._data) ** 0.5

print("\n--- Custom Vector ---")
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"|v1| = {abs(v1):.2f}")
print(f"len(v1) = {len(v1)}")
print(f"v1[0] = {v1[0]}")
print(f"v1 == v2? {v1 == v2}")
print(f"bool(Vector(0,0,0))? {bool(Vector(0, 0, 0))}")


# KEY TAKEAWAYS:
# - Magic methods let your objects work with Python's built-in operations
# - __str__: user-friendly string (print)  |  __repr__: developer string (debug)
# - Arithmetic: __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__
# - Comparison: __eq__, __ne__, __lt__, __le__, __gt__, __ge__
# - Container: __len__, __getitem__, __setitem__, __contains__, __iter__
# - __call__: makes an object callable like a function
# - __bool__: controls truthiness  |  __abs__: controls abs()
# - Return NotImplemented (not raise!) if operation isn't supported
