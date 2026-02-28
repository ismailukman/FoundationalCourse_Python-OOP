#!/usr/bin/env python

# =============================================================================
# MODULE 09: DECORATORS AND PROPERTY - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Logging Decorator ----
# Create a decorator 'log_calls' that:
#   - Prints function name, arguments, and return value
#   - Tracks how many times each function has been called
#   - Has a .call_count attribute on the decorated function
#
# Expected Output:
# [CALL #1] add(3, 5) -> 8
# [CALL #2] add(10, 20) -> 30
# [CALL #1] multiply(4, 6) -> 24
# add was called 2 times
# multiply was called 1 times

# YOUR CODE HERE:




# ---- Question 2: Property-Driven User Profile ----
# Create a class 'UserProfile' with full property-based validation:
#   - username: 3-20 chars, alphanumeric only
#   - email: must contain @ and .
#   - age: 13-120 (minimum age for platform)
#   - bio: max 200 characters
#   - Read-only: display_name (username + age badge)
#
# Expected Output:
# Profile: alice123 | alice@email.com | Age: 25
# Display: alice123 [25]
# Bio: "Python enthusiast and OOP learner"
# Updated username to: alice_dev
# Error: Username must be alphanumeric (3-20 chars)
# Error: Age must be between 13 and 120

# YOUR CODE HERE:




# ---- Question 3: Smart House System ----
# Create a class 'SmartDevice' using @property for state management:
#   - Properties: name, is_on (bool), brightness (0-100), temperature (16-30)
#   - All setters should validate and print status changes
#   - Read-only: energy_usage (based on brightness and on/off)
#   - Method: reset() restores defaults
#
# Expected Output:
# Living Room Light: OFF | Brightness: 50 | Temp: 22°C | Energy: 0W
# Turning ON Living Room Light
# Living Room Light: ON | Brightness: 50 | Temp: 22°C | Energy: 50W
# Setting brightness to 80
# Living Room Light: ON | Brightness: 80 | Temp: 22°C | Energy: 80W
# Error: Brightness must be 0-100
# Setting temperature to 25°C
# Error: Temperature must be 16-30°C

# YOUR CODE HERE:




# ---- Question 4: Caching Decorator ----
# Create a decorator 'cache' that stores results of function calls.
# If the same arguments are passed again, return the cached result.
# Add a .cache_info() method showing hits, misses, and cache size.
#
# Expected Output:
# Computing fib(10)...
# fib(10) = 55 (first call)
# fib(10) = 55 (cached!)
# fib(20) = 6765 (first call)
# Cache info: {'hits': 1, 'misses': 2, 'size': 2}

# YOUR CODE HERE:




# ---- Question 5: Property-Based State Machine ----
# Create a class 'Order' that uses @property to enforce state transitions:
#   - States: "pending" -> "confirmed" -> "shipped" -> "delivered"
#   - Property: status (with setter that validates transitions)
#   - Invalid transitions should raise ValueError
#   - Read-only properties: is_complete, can_cancel
#   - Method: cancel() only works if pending or confirmed
#   - Each state change records timestamp
#
# Expected Output:
# Order #1: Widget | Status: pending
# Status changed: pending -> confirmed
# Status changed: confirmed -> shipped
# Status changed: shipped -> delivered
# Order complete: True
# Can cancel: False
# 
# Order #2: Gadget | Status: pending
# Cancelled order!
# 
# Error: Cannot transition from pending to delivered
# Error: Cannot transition from shipped to confirmed

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# import functools
# def log_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.call_count += 1
#         args_str = ", ".join(str(a) for a in args)
#         result = func(*args, **kwargs)
#         print(f"[CALL #{wrapper.call_count}] {func.__name__}({args_str}) -> {result}")
#         return result
#     wrapper.call_count = 0
#     return wrapper
#
# @log_calls
# def add(a, b):
#     return a + b
#
# @log_calls
# def multiply(a, b):
#     return a * b
#
# add(3, 5)
# add(10, 20)
# multiply(4, 6)
# print(f"add was called {add.call_count} times")
# print(f"multiply was called {multiply.call_count} times")


# # Question 2:
# class UserProfile:
#     def __init__(self, username, email, age, bio=""):
#         self.username = username
#         self.email = email
#         self.age = age
#         self.bio = bio
#
#     @property
#     def username(self):
#         return self._username
#
#     @username.setter
#     def username(self, value):
#         if not value.replace('_', '').isalnum() or not (3 <= len(value) <= 20):
#             print("Error: Username must be alphanumeric (3-20 chars)")
#             return
#         self._username = value
#         print(f"Updated username to: {value}")
#
#     @property
#     def email(self):
#         return self._email
#
#     @email.setter
#     def email(self, value):
#         if '@' not in value or '.' not in value:
#             print("Error: Invalid email format")
#             return
#         self._email = value
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if not (13 <= value <= 120):
#             print("Error: Age must be between 13 and 120")
#             return
#         self._age = value
#
#     @property
#     def bio(self):
#         return self._bio
#
#     @bio.setter
#     def bio(self, value):
#         if len(value) > 200:
#             print("Error: Bio must be 200 characters or less")
#             return
#         self._bio = value
#
#     @property
#     def display_name(self):
#         return f"{self._username} [{self._age}]"
#
#     def show(self):
#         print(f"Profile: {self._username} | {self._email} | Age: {self._age}")
#         print(f"Display: {self.display_name}")
#         if self._bio:
#             print(f'Bio: "{self._bio}"')
#
# u = UserProfile("alice123", "alice@email.com", 25, "Python enthusiast and OOP learner")
# u.show()
# u.username = "alice_dev"
# u.username = "ab"
# u.age = 5


# # Question 3:
# class SmartDevice:
#     def __init__(self, name):
#         self._name = name
#         self._is_on = False
#         self._brightness = 50
#         self._temperature = 22
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def is_on(self):
#         return self._is_on
#
#     @is_on.setter
#     def is_on(self, value):
#         self._is_on = value
#         state = "ON" if value else "OFF"
#         print(f"Turning {state} {self._name}")
#
#     @property
#     def brightness(self):
#         return self._brightness
#
#     @brightness.setter
#     def brightness(self, value):
#         if not (0 <= value <= 100):
#             print("Error: Brightness must be 0-100")
#             return
#         print(f"Setting brightness to {value}")
#         self._brightness = value
#
#     @property
#     def temperature(self):
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         if not (16 <= value <= 30):
#             print(f"Error: Temperature must be 16-30°C")
#             return
#         print(f"Setting temperature to {value}°C")
#         self._temperature = value
#
#     @property
#     def energy_usage(self):
#         return self._brightness if self._is_on else 0
#
#     def status(self):
#         state = "ON" if self._is_on else "OFF"
#         print(f"{self._name}: {state} | Brightness: {self._brightness} | Temp: {self._temperature}°C | Energy: {self.energy_usage}W")
#
#     def reset(self):
#         self._is_on = False
#         self._brightness = 50
#         self._temperature = 22
#
# d = SmartDevice("Living Room Light")
# d.status()
# d.is_on = True
# d.status()
# d.brightness = 80
# d.status()
# d.brightness = 150
# d.temperature = 25
# d.temperature = 35


# # Question 4:
# def cache(func):
#     _cache = {}
#     _hits = 0
#     _misses = 0
#
#     def wrapper(*args):
#         nonlocal _hits, _misses
#         if args in _cache:
#             _hits += 1
#             return _cache[args]
#         _misses += 1
#         result = func(*args)
#         _cache[args] = result
#         return result
#
#     def cache_info():
#         return {"hits": _hits, "misses": _misses, "size": len(_cache)}
#
#     wrapper.cache_info = cache_info
#     return wrapper
#
# @cache
# def fib(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
# print(f"fib(10) = {fib(10)} (first call)")
# print(f"fib(10) = {fib(10)} (cached!)")
# print(f"fib(20) = {fib(20)} (first call)")
# print(f"Cache info: {fib.cache_info()}")


# # Question 5:
# from datetime import datetime
# class Order:
#     VALID_TRANSITIONS = {
#         "pending": ["confirmed", "cancelled"],
#         "confirmed": ["shipped", "cancelled"],
#         "shipped": ["delivered"],
#         "delivered": [],
#         "cancelled": []
#     }
#
#     def __init__(self, order_id, item):
#         self.order_id = order_id
#         self.item = item
#         self._status = "pending"
#         self.history = [("pending", datetime.now())]
#
#     @property
#     def status(self):
#         return self._status
#
#     @status.setter
#     def status(self, new_status):
#         if new_status not in Order.VALID_TRANSITIONS.get(self._status, []):
#             print(f"Error: Cannot transition from {self._status} to {new_status}")
#             return
#         old = self._status
#         self._status = new_status
#         self.history.append((new_status, datetime.now()))
#         print(f"Status changed: {old} -> {new_status}")
#
#     @property
#     def is_complete(self):
#         return self._status == "delivered"
#
#     @property
#     def can_cancel(self):
#         return self._status in ["pending", "confirmed"]
#
#     def cancel(self):
#         if self.can_cancel:
#             self.status = "cancelled"
#             print("Cancelled order!")
#         else:
#             print(f"Cannot cancel order in '{self._status}' state")
#
#     def show(self):
#         print(f"Order #{self.order_id}: {self.item} | Status: {self._status}")
#
# o1 = Order(1, "Widget")
# o1.show()
# o1.status = "confirmed"
# o1.status = "shipped"
# o1.status = "delivered"
# print(f"Order complete: {o1.is_complete}")
# print(f"Can cancel: {o1.can_cancel}")
# print()
# o2 = Order(2, "Gadget")
# o2.show()
# o2.cancel()
# print()
# o3 = Order(3, "Test")
# o3.status = "delivered"
# o4 = Order(4, "Test")
# o4.status = "confirmed"
# o4.status = "shipped"
# o4.status = "confirmed"
