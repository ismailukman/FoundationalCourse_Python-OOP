#!/usr/bin/env python

# =============================================================================
# MODULE 07: POLYMORPHISM - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Shape Calculator ----
# Create classes: Circle, Square, Triangle, all with area() and perimeter().
# Write a function report(shapes) that prints a table of all shapes.
#
# Expected Output:
# Shape Report:
# +-----------------+----------+-----------+
# | Shape           |     Area | Perimeter |
# +-----------------+----------+-----------+
# | Circle (r=5)    |    78.54 |     31.42 |
# | Square (s=4)    |    16.00 |     16.00 |
# | Triangle (3,4,5)|     6.00 |     12.00 |
# +-----------------+----------+-----------+
# Total area: 100.54

# YOUR CODE HERE:




# ---- Question 2: File Exporter System ----
# Create classes representing different export formats:
#   - CSVExporter: export(data) formats as CSV
#   - JSONExporter: export(data) formats as JSON-like string
#   - HTMLExporter: export(data) formats as HTML table
# data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
#
# Expected Output:
# === CSV Export ===
# name,age
# Alice,30
# Bob,25
#
# === JSON Export ===
# [
#   {"name": "Alice", "age": 30},
#   {"name": "Bob", "age": 25}
# ]
#
# === HTML Export ===
# <table>
#   <tr><th>name</th><th>age</th></tr>
#   <tr><td>Alice</td><td>30</td></tr>
#   <tr><td>Bob</td><td>25</td></tr>
# </table>

# YOUR CODE HERE:




# ---- Question 3: Transport System ----
# Create vehicle classes with a common interface:
#   - Car: travel(distance), fuel_needed(distance), cost(distance)
#   - Bicycle: same methods
#   - Airplane: same methods
# Write a function plan_trip(vehicles, distance) showing all options.
#
# Expected Output:
# Trip Planning: 100 km
# Car: 3.5h | Fuel: 8.33L | Cost: $16.67
# Bicycle: 5.0h | Fuel: 0.00L | Cost: $0.00
# Airplane: 0.2h | Fuel: 500.00L | Cost: $250.00
# Cheapest: Bicycle ($0.00)
# Fastest: Airplane (0.2h)

# YOUR CODE HERE:




# ---- Question 4: Sort with Custom Objects ----
# Create a class 'Student' with name, gpa.
# Implement __lt__, __eq__, __repr__ so students can be sorted by GPA.
# Demonstrate polymorphism with Python's built-in sorted().
#
# Expected Output:
# Before sorting:
# [Student(Charlie, 3.5), Student(Alice, 3.9), Student(Bob, 3.2), Student(Diana, 3.7)]
# After sorting by GPA:
# [Student(Bob, 3.2), Student(Charlie, 3.5), Student(Diana, 3.7), Student(Alice, 3.9)]
# Top student: Student(Alice, 3.9)
# Students with GPA >= 3.5: Charlie, Diana, Alice

# YOUR CODE HERE:




# ---- Question 5: Plugin System ----
# Create a plugin architecture:
#   - Base: Plugin with methods activate(), deactivate(), execute(data)
#   - UpperCasePlugin: converts text to uppercase
#   - ReversePlugin: reverses the text
#   - CensorPlugin: replaces "bad" words with "***"
# Process text through a pipeline of plugins.
#
# Expected Output:
# Original: "Hello World this is a bad example"
# After UpperCasePlugin: "HELLO WORLD THIS IS A BAD EXAMPLE"
# After ReversePlugin: "ELPMAXE DAB A SI SIHT DLROW OLLEH"
# After CensorPlugin: "ELPMAXE *** A SI SIHT DLROW OLLEH"
# 
# Pipeline processing:
# Input: "This is bad and ugly bad code"
# -> UpperCasePlugin -> "THIS IS BAD AND UGLY BAD CODE"
# -> CensorPlugin -> "THIS IS *** AND UGLY *** CODE"
# -> ReversePlugin -> "EDOC *** YLGU DNA *** SI SIHT"

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#     def name(self):
#         return f"Circle (r={self.radius})"
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side ** 2
#     def perimeter(self):
#         return 4 * self.side
#     def name(self):
#         return f"Square (s={self.side})"
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c
#     def area(self):
#         s = (self.a + self.b + self.c) / 2
#         return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
#     def perimeter(self):
#         return self.a + self.b + self.c
#     def name(self):
#         return f"Triangle ({self.a},{self.b},{self.c})"
#
# def report(shapes):
#     print("Shape Report:")
#     print(f"+-{'-'*15}-+-{'-'*8}-+-{'-'*9}-+")
#     print(f"| {'Shape':<15} | {'Area':>8} | {'Perimeter':>9} |")
#     print(f"+-{'-'*15}-+-{'-'*8}-+-{'-'*9}-+")
#     total = 0
#     for s in shapes:
#         total += s.area()
#         print(f"| {s.name():<15} | {s.area():>8.2f} | {s.perimeter():>9.2f} |")
#     print(f"+-{'-'*15}-+-{'-'*8}-+-{'-'*9}-+")
#     print(f"Total area: {total:.2f}")
#
# report([Circle(5), Square(4), Triangle(3, 4, 5)])


# # Question 2:
# class CSVExporter:
#     def export(self, data):
#         keys = data[0].keys()
#         lines = [",".join(keys)]
#         for row in data:
#             lines.append(",".join(str(v) for v in row.values()))
#         return "\n".join(lines)
#
# class JSONExporter:
#     def export(self, data):
#         lines = ["["]
#         for i, row in enumerate(data):
#             items = ", ".join(f'"{k}": {f"{v}" if isinstance(v,int) else f"{chr(34)}{v}{chr(34)}"}' for k,v in row.items())
#             comma = "," if i < len(data)-1 else ""
#             lines.append(f"  {{{items}}}{comma}")
#         lines.append("]")
#         return "\n".join(lines)
#
# class HTMLExporter:
#     def export(self, data):
#         keys = data[0].keys()
#         lines = ["<table>"]
#         lines.append("  <tr>" + "".join(f"<th>{k}</th>" for k in keys) + "</tr>")
#         for row in data:
#             lines.append("  <tr>" + "".join(f"<td>{v}</td>" for v in row.values()) + "</tr>")
#         lines.append("</table>")
#         return "\n".join(lines)
#
# data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
# exporters = [("CSV", CSVExporter()), ("JSON", JSONExporter()), ("HTML", HTMLExporter())]
# for name, exp in exporters:
#     print(f"=== {name} Export ===")
#     print(exp.export(data))
#     print()


# # Question 3:
# class Car:
#     speed = 80
#     fuel_rate = 12
#     fuel_cost = 2.0
#     def travel(self, dist): return round(dist / self.speed, 1)
#     def fuel_needed(self, dist): return round(dist / self.fuel_rate, 2)
#     def cost(self, dist): return round(self.fuel_needed(dist) * self.fuel_cost, 2)
#     def name(self): return "Car"
#
# class Bicycle:
#     speed = 20
#     def travel(self, dist): return round(dist / self.speed, 1)
#     def fuel_needed(self, dist): return 0.0
#     def cost(self, dist): return 0.0
#     def name(self): return "Bicycle"
#
# class Airplane:
#     speed = 500
#     fuel_rate = 0.2
#     fuel_cost = 0.5
#     def travel(self, dist): return round(dist / self.speed, 1)
#     def fuel_needed(self, dist): return round(dist / self.fuel_rate, 2)
#     def cost(self, dist): return round(self.fuel_needed(dist) * self.fuel_cost, 2)
#     def name(self): return "Airplane"
#
# def plan_trip(vehicles, dist):
#     print(f"Trip Planning: {dist} km")
#     results = []
#     for v in vehicles:
#         t, f, c = v.travel(dist), v.fuel_needed(dist), v.cost(dist)
#         print(f"{v.name()}: {t}h | Fuel: {f:.2f}L | Cost: ${c:.2f}")
#         results.append((v.name(), t, c))
#     cheapest = min(results, key=lambda x: x[2])
#     fastest = min(results, key=lambda x: x[1])
#     print(f"Cheapest: {cheapest[0]} (${cheapest[2]:.2f})")
#     print(f"Fastest: {fastest[0]} ({fastest[1]}h)")
#
# plan_trip([Car(), Bicycle(), Airplane()], 100)


# # Question 4:
# class Student:
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#     def __lt__(self, other):
#         return self.gpa < other.gpa
#     def __eq__(self, other):
#         return self.gpa == other.gpa
#     def __repr__(self):
#         return f"Student({self.name}, {self.gpa})"
#
# students = [Student("Charlie", 3.5), Student("Alice", 3.9),
#             Student("Bob", 3.2), Student("Diana", 3.7)]
# print("Before sorting:")
# print(students)
# print("After sorting by GPA:")
# ss = sorted(students)
# print(ss)
# print(f"Top student: {max(students)}")
# high = [s.name for s in students if s.gpa >= 3.5]
# print(f"Students with GPA >= 3.5: {', '.join(high)}")


# # Question 5:
# class Plugin:
#     def activate(self):
#         print(f"{self.__class__.__name__} activated")
#     def deactivate(self):
#         print(f"{self.__class__.__name__} deactivated")
#     def execute(self, data):
#         raise NotImplementedError
#
# class UpperCasePlugin(Plugin):
#     def execute(self, data):
#         return data.upper()
#
# class ReversePlugin(Plugin):
#     def execute(self, data):
#         return data[::-1]
#
# class CensorPlugin(Plugin):
#     def __init__(self, bad_words=None):
#         self.bad_words = bad_words or ["BAD", "UGLY"]
#     def execute(self, data):
#         result = data
#         for word in self.bad_words:
#             result = result.replace(word, "***")
#         return result
#
# text = "Hello World this is a bad example"
# print(f'Original: "{text}"')
# for p in [UpperCasePlugin(), ReversePlugin(), CensorPlugin()]:
#     print(f'After {p.__class__.__name__}: "{p.execute(text.upper())}"')
#
# print("\nPipeline processing:")
# pipeline = [UpperCasePlugin(), CensorPlugin(), ReversePlugin()]
# data = "This is bad and ugly bad code"
# print(f'Input: "{data}"')
# for p in pipeline:
#     data = p.execute(data)
#     print(f'-> {p.__class__.__name__} -> "{data}"')
