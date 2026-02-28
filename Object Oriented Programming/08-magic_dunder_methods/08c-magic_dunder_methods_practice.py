#!/usr/bin/env python

# =============================================================================
# MODULE 08: SPECIAL (MAGIC / DUNDER) METHODS - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Custom Fraction Class ----
# Create a class 'Fraction' with numerator and denominator.
# Implement: __add__, __sub__, __mul__, __truediv__, __eq__, __lt__,
#            __repr__, __str__, __float__
# Auto-simplify fractions using GCD.
#
# Expected Output:
# 1/2 + 1/3 = 5/6
# 3/4 - 1/4 = 1/2
# 2/3 * 3/4 = 1/2
# 1/2 / 1/4 = 2/1
# 1/2 == 2/4? True
# 1/3 < 1/2? True
# float(3/4) = 0.75

# YOUR CODE HERE:




# ---- Question 2: Matrix Class ----
# Create a 2x2 Matrix class with:
#   - __add__: matrix addition
#   - __mul__: matrix multiplication
#   - __eq__: compare matrices
#   - __repr__, __str__: display matrices
#   - __getitem__: access elements with matrix[row][col]
#
# Expected Output:
# Matrix A:
# | 1  2 |
# | 3  4 |
# Matrix B:
# | 5  6 |
# | 7  8 |
# A + B:
# |  6   8 |
# | 10  12 |
# A * B:
# | 19  22 |
# | 43  50 |

# YOUR CODE HERE:




# ---- Question 3: Custom Range Iterator ----
# Create a class 'FloatRange' that works like range() but with floats.
# Implement: __iter__, __next__, __len__, __contains__, __repr__
#
# Expected Output:
# FloatRange(0.0, 1.0, step=0.2):
# 0.0, 0.2, 0.4, 0.6, 0.8
# Length: 5
# Contains 0.4? True
# Contains 0.5? False
# As list: [0.0, 0.2, 0.4, 0.6, 0.8]

# YOUR CODE HERE:




# ---- Question 4: Smart Dictionary ----
# Create a class 'SmartDict' that wraps a dictionary with magic methods:
#   - __getitem__, __setitem__, __delitem__: dict-like access
#   - __contains__: 'key in smart_dict'
#   - __len__: number of items
#   - __iter__: iterate over keys
#   - __add__: merge two SmartDicts
#   - __repr__, __str__: display contents
#   - __call__: filter items by a function
#
# Expected Output:
# SmartDict({'name': 'Alice', 'age': 30, 'city': 'NYC'})
# name: Alice
# age: 30
# Contains 'name'? True
# Length: 3
# Merged: SmartDict({'name': 'Alice', 'age': 30, 'city': 'NYC', 'job': 'Dev'})
# Filtered (str values): {'name': 'Alice', 'city': 'NYC'}

# YOUR CODE HERE:




# ---- Question 5: Chainable Calculator ----
# Create a 'Calc' class where operations can be chained using magic methods.
# Support: +, -, *, /, calling (reset), str, repr, int, float
#
# Expected Output:
# Calc(0) + 10 = 10
# Calc(10) * 3 = 30
# Calc(30) - 5 = 25
# Calc(25) / 5 = 5.0
# int(result) = 5
# float(result) = 5.0
# Chain: Calc(0) + 10 * 2 - 5 = 15
# Reset: Calc(0)(42) = 42

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# from math import gcd
# class Fraction:
#     def __init__(self, num, den):
#         if den == 0:
#             raise ValueError("Denominator cannot be zero")
#         g = gcd(abs(num), abs(den))
#         self.num = num // g
#         self.den = den // g
#
#     def __add__(self, other):
#         return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)
#
#     def __sub__(self, other):
#         return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)
#
#     def __mul__(self, other):
#         return Fraction(self.num * other.num, self.den * other.den)
#
#     def __truediv__(self, other):
#         return Fraction(self.num * other.den, self.den * other.num)
#
#     def __eq__(self, other):
#         return self.num == other.num and self.den == other.den
#
#     def __lt__(self, other):
#         return self.num * other.den < other.num * self.den
#
#     def __float__(self):
#         return self.num / self.den
#
#     def __repr__(self):
#         return f"Fraction({self.num}, {self.den})"
#
#     def __str__(self):
#         return f"{self.num}/{self.den}"
#
# f1, f2, f3, f4 = Fraction(1,2), Fraction(1,3), Fraction(3,4), Fraction(1,4)
# print(f"{f1} + {f2} = {f1+f2}")
# print(f"{f3} - {f4} = {f3-f4}")
# print(f"2/3 * 3/4 = {Fraction(2,3)*f3}")
# print(f"{f1} / {f4} = {f1/f4}")
# print(f"{f1} == {Fraction(2,4)}? {f1 == Fraction(2,4)}")
# print(f"{f2} < {f1}? {f2 < f1}")
# print(f"float(3/4) = {float(f3)}")


# # Question 2:
# class Matrix:
#     def __init__(self, data):
#         self.data = data
#         self.rows = len(data)
#         self.cols = len(data[0])
#
#     def __add__(self, other):
#         result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         return Matrix(result)
#
#     def __mul__(self, other):
#         result = [[sum(self.data[i][k]*other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
#         return Matrix(result)
#
#     def __eq__(self, other):
#         return self.data == other.data
#
#     def __getitem__(self, index):
#         return self.data[index]
#
#     def __repr__(self):
#         return f"Matrix({self.data})"
#
#     def __str__(self):
#         lines = []
#         for row in self.data:
#             lines.append("| " + "  ".join(f"{v:>2}" for v in row) + " |")
#         return "\n".join(lines)
#
# a = Matrix([[1,2],[3,4]])
# b = Matrix([[5,6],[7,8]])
# print("Matrix A:")
# print(a)
# print("Matrix B:")
# print(b)
# print("A + B:")
# print(a + b)
# print("A * B:")
# print(a * b)


# # Question 3:
# class FloatRange:
#     def __init__(self, start, stop, step=0.1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __iter__(self):
#         self._current = self.start
#         return self
#
#     def __next__(self):
#         if self._current >= self.stop - 1e-10:
#             raise StopIteration
#         value = round(self._current, 10)
#         self._current += self.step
#         return value
#
#     def __len__(self):
#         import math
#         return math.ceil((self.stop - self.start) / self.step)
#
#     def __contains__(self, value):
#         return any(abs(x - value) < 1e-9 for x in self)
#
#     def __repr__(self):
#         return f"FloatRange({self.start}, {self.stop}, step={self.step})"
#
# fr = FloatRange(0.0, 1.0, 0.2)
# print(f"{fr}:")
# print(", ".join(f"{x}" for x in fr))
# print(f"Length: {len(fr)}")
# print(f"Contains 0.4? {0.4 in fr}")
# print(f"Contains 0.5? {0.5 in fr}")
# print(f"As list: {list(fr)}")


# # Question 4:
# class SmartDict:
#     def __init__(self, data=None):
#         self._data = data if data is not None else {}
#
#     def __getitem__(self, key):
#         return self._data[key]
#
#     def __setitem__(self, key, value):
#         self._data[key] = value
#
#     def __delitem__(self, key):
#         del self._data[key]
#
#     def __contains__(self, key):
#         return key in self._data
#
#     def __len__(self):
#         return len(self._data)
#
#     def __iter__(self):
#         return iter(self._data)
#
#     def __add__(self, other):
#         merged = {**self._data, **other._data}
#         return SmartDict(merged)
#
#     def __repr__(self):
#         return f"SmartDict({self._data})"
#
#     def __str__(self):
#         return str(self._data)
#
#     def __call__(self, func):
#         return {k: v for k, v in self._data.items() if func(v)}
#
# sd = SmartDict({"name": "Alice", "age": 30, "city": "NYC"})
# print(repr(sd))
# for key in sd:
#     print(f"{key}: {sd[key]}")
# print(f"Contains 'name'? {'name' in sd}")
# print(f"Length: {len(sd)}")
# sd2 = SmartDict({"job": "Dev"})
# print(f"Merged: {repr(sd + sd2)}")
# print(f"Filtered (str values): {sd(lambda v: isinstance(v, str))}")


# # Question 5:
# class Calc:
#     def __init__(self, value=0):
#         self.value = value
#
#     def __add__(self, other):
#         return Calc(self.value + other)
#
#     def __sub__(self, other):
#         return Calc(self.value - other)
#
#     def __mul__(self, other):
#         return Calc(self.value * other)
#
#     def __truediv__(self, other):
#         return Calc(self.value / other)
#
#     def __call__(self, value):
#         return Calc(value)
#
#     def __int__(self):
#         return int(self.value)
#
#     def __float__(self):
#         return float(self.value)
#
#     def __repr__(self):
#         return f"Calc({self.value})"
#
#     def __str__(self):
#         return str(self.value)
#
# c = Calc()
# print(f"Calc(0) + 10 = {c + 10}")
# c = c + 10
# print(f"Calc(10) * 3 = {c * 3}")
# c = c * 3
# print(f"Calc(30) - 5 = {c - 5}")
# c = c - 5
# print(f"Calc(25) / 5 = {c / 5}")
# c = c / 5
# print(f"int(result) = {int(c)}")
# print(f"float(result) = {float(c)}")
# chain = Calc() + 10
# chain = chain * 2
# chain = chain - 5
# print(f"Chain: Calc(0) + 10 * 2 - 5 = {chain}")
# print(f"Reset: Calc(0)(42) = {Calc()(42)}")
