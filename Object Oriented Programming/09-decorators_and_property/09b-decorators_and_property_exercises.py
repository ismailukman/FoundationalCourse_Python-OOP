#!/usr/bin/env python

# =============================================================================
# MODULE 09: DECORATORS AND PROPERTY - EXERCISES
# =============================================================================
# Test your understanding of decorators and the @property pattern.
# =============================================================================


# ---- Exercise 1: Write a Simple Decorator ----
# Create a decorator 'bold' that wraps a function's string return value
# in HTML bold tags: <b>result</b>
# Create a decorator 'italic' that wraps in <i>result</i>
# Test stacking both: @bold @italic should produce <b><i>result</i></b>

# YOUR CODE HERE:




# ---- Exercise 2: Timer Decorator with Arguments ----
# Create a decorator 'repeat(n)' that calls a function n times
# and collects all return values in a list.
# Usage: @repeat(3) -> calls the function 3 times

# YOUR CODE HERE:




# ---- Exercise 3: @property Basics ----
# Create a class 'Person' with:
#   - Private attributes: _first_name, _last_name, _birth_year
#   - Properties: first_name, last_name (with getters and setters)
#   - Read-only property: full_name (computed)
#   - Read-only property: age (computed from birth_year and current year)
#   - Setter validation: names must be non-empty strings
# Test: create a person and change their name using properties.

# YOUR CODE HERE:




# ---- Exercise 4: Predict the Output ----

def double_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

def add_ten(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 10
    return wrapper

@double_result
@add_ten
def get_value(x):
    return x

# What does get_value(5) return?
# Step through it: get_value = double_result(add_ten(get_value))
# Prediction: ___
print(get_value(5))

@add_ten
@double_result
def get_value2(x):
    return x

# What about get_value2(5)?
# Prediction: ___
print(get_value2(5))


# ---- Exercise 5: Property-Based Validation Class ----
# Create a class 'BankAccount' with:
#   - Property: owner (must be non-empty string)
#   - Property: balance (must be >= 0, read-only from outside)
#   - Property: account_type (must be "checking" or "savings")
#   - Method: deposit(amount) and withdraw(amount)
#   - Read-only property: status ("Low" if < 100, "Normal" if < 10000, "Premium")

# YOUR CODE HERE:




# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: def bold(func):
#                 def wrapper(*args, **kwargs):
#                     return f"<b>{func(*args, **kwargs)}</b>"
#                 return wrapper
#
# Exercise 2: def repeat(n):
#                 def decorator(func):
#                     def wrapper(*args, **kwargs):
#                         return [func(*args, **kwargs) for _ in range(n)]
#                     return wrapper
#                 return decorator
#
# Exercise 3: @property
#             def first_name(self):
#                 return self._first_name
#             @first_name.setter
#             def first_name(self, value):
#                 if not value or not isinstance(value, str):
#                     raise ValueError("Name must be non-empty string")
#                 self._first_name = value
#
# Exercise 4: get_value(5): add_ten first (5+10=15), then double (15*2=30)
#             get_value2(5): double first (5*2=10), then add_ten (10+10=20)
#             Decorators apply bottom-up, but execute top-down
#
# Exercise 5: Use @property and @x.setter pattern for each validated attribute
# =============================================================================
