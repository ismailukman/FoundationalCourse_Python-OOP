#!/usr/bin/env python

# =============================================================================
# MODULE 08: SPECIAL (MAGIC / DUNDER) METHODS - EXERCISES
# =============================================================================
# Test your understanding of magic methods.
# =============================================================================


# ---- Exercise 1: __str__ and __repr__ ----
# Create a class 'Book' with title, author, year.
# __repr__ should return: Book('Title', 'Author', Year)
# __str__ should return: "Title" by Author (Year)
# Test both with print() and repr().

# YOUR CODE HERE:




# ---- Exercise 2: Arithmetic Operators ----
# Create a class 'Temperature' with degrees and scale ("C" or "F").
# Implement:
#   __add__: Temperature(20, "C") + Temperature(10, "C") = Temperature(30, "C")
#   __sub__: Temperature(30, "C") - Temperature(10, "C") = Temperature(20, "C")
#   __mul__: Temperature(10, "C") * 2 = Temperature(20, "C")
#   __eq__: Temperature(100, "C") == Temperature(212, "F") (convert to compare!)
# Raise error if adding different scales.

# YOUR CODE HERE:




# ---- Exercise 3: Predict the Output ----

class Box:
    def __init__(self, *items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, idx):
        return self.items[idx]

    def __add__(self, other):
        return Box(*(self.items + other.items))

    def __bool__(self):
        return len(self.items) > 0

    def __repr__(self):
        return f"Box({self.items})"

b1 = Box("apple", "banana")
b2 = Box("cherry")
b3 = Box()

# Prediction: ___
print(len(b1))

# Prediction: ___
print("apple" in b1)

# Prediction: ___
print(b1[1])

# Prediction: ___
print(b1 + b2)

# Prediction: ___
print(bool(b3))

# Prediction: ___
if b1:
    print("b1 is truthy")

# Prediction: ___
print(b1[-1])


# ---- Exercise 4: Implement __call__ ----
# Create a class 'Accumulator' that:
#   - Starts with a value of 0
#   - When called with a number, ADDS it to the value
#   - Returns the new total
#   - Implements __repr__ to show current value
# Usage: acc = Accumulator(); acc(5); acc(3); acc(2)  # -> 10

# YOUR CODE HERE:




# ---- Exercise 5: Full Container Class ----
# Create a class 'SortedList' that:
#   - Maintains items in sorted order at all times
#   - __len__, __getitem__, __contains__, __iter__, __repr__
#   - Method: add(item) inserts in correct sorted position
#   - Method: remove(item) removes first occurrence
# Test: add 5, 2, 8, 1, 9 — list should always be [1, 2, 5, 8, 9]

# YOUR CODE HERE:




# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: def __repr__(self): return f"Book('{self.title}', '{self.author}', {self.year})"
#             def __str__(self): return f'"{self.title}" by {self.author} ({self.year})'
#
# Exercise 2: Convert to same scale before comparing.
#             C_to_F: c * 9/5 + 32;  F_to_C: (f - 32) * 5/9
#
# Exercise 3: len=2, "apple" in b1=True, b1[1]="banana",
#             b1+b2=Box(['apple','banana','cherry']), bool(b3)=False,
#             b1 is truthy, b1[-1]="banana"
#
# Exercise 4: def __call__(self, value):
#                 self.total += value
#                 return self.total
#
# Exercise 5: Use bisect module or insert at correct position manually
#             import bisect; bisect.insort(self._items, item)
# =============================================================================
