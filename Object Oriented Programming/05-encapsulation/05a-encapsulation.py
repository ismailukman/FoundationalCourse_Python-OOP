#!/usr/bin/env python

# =============================================================================
# MODULE 05: ENCAPSULATION (Intermediate)
# =============================================================================
#
# GOALS:
#   1. Understand what encapsulation means and why it matters
#   2. Learn Python's naming conventions for access control
#   3. Use public, protected (_), and private (__) attributes
#   4. Understand name mangling and how Python handles "private" members
#   5. Implement getters and setters manually
#
# ENCAPSULATION is one of the four pillars of OOP. It means:
#   - Bundling data (attributes) and methods that operate on that data together
#   - Restricting direct access to some components (data hiding)
#   - Providing controlled access through methods (getters/setters)
#
# WHY? To prevent accidental modification of data, enforce validation,
# and make code more maintainable.
#
# PYTHON ACCESS CONVENTIONS:
#   public:    name       -> accessible everywhere (default)
#   protected: _name      -> convention: "internal use" (still accessible)
#   private:   __name     -> name mangling: _ClassName__name (harder to access)
#
# =============================================================================

# ---- Example 1: The Problem Without Encapsulation ----
print("\nExample 1") 
class BankAccountUnsafe:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance     # Public! Anyone can change it!

acc = BankAccountUnsafe("Alice", 1000)
acc.balance = -500    # Oops! No validation! Balance is now negative!
print(f"Balance: {acc.balance}")  # -500 - This shouldn't be allowed!


# ---- Example 2: Public, Protected, and Private ----
print("\nExample 2") 
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public - anyone can access
        self._salary = salary       # Protected - convention: internal use only
        self.__ssn = ssn            # Private - name mangling applied

e = Employee("Alice", 70000, "123-45-6789")

# Public: works fine
print(f"Name: {e.name}")

# Protected: works but signals "don't touch this from outside"
print(f"Salary: {e._salary}")       # Works, but it's a convention warning

# Private: direct access fails!
try:
    print(e.__ssn)
except AttributeError as err:
    print(f"Cannot access __ssn: {err}")

# But Python doesn't truly hide it - name mangling renames it:
print(f"SSN via mangling: {e._Employee__ssn}")  # Works but bad practice!

# Let's see what's in the instance namespace:
print(f"\nNamespace: {e.__dict__}")
# {'name': 'Alice', '_salary': 70000, '_Employee__ssn': '123-45-6789'}


# ---- Example 3: Proper Encapsulation with Getters and Setters ----
print("\nExample 3") 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    # Getter - controlled read access
    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    # Setter with validation - controlled write access
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive!")
            return
        self.__balance += amount
        print(f"Deposited ${amount:.2f}. Balance: ${self.__balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
            return
        if amount > self.__balance:
            print(f"Error: Insufficient funds! Balance: ${self.__balance:.2f}")
            return
        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}. Balance: ${self.__balance:.2f}")

print("\n--- Encapsulated Bank Account ---")
acc = BankAccount("Bob", 1000)
print(f"Owner: {acc.get_owner()}")
print(f"Balance: ${acc.get_balance():.2f}")
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)     # Blocked!
acc.deposit(-100)      # Blocked!


# ---- Example 4: Why Encapsulation Matters ----
print("\nExample 4") 
class Temperature:
    def __init__(self, celsius):
        self.__celsius = None     # Initialise first
        self.set_celsius(celsius) # Use setter for validation

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, value):
        if value < -273.15:    # Absolute zero
            raise ValueError(f"Temperature {value}°C is below absolute zero!")
        self.__celsius = value

    def get_fahrenheit(self):
        return self.__celsius * 9/5 + 32

print("\n--- Temperature with Validation ---")
t = Temperature(100)
print(f"{t.get_celsius()}°C = {t.get_fahrenheit()}°F")

t.set_celsius(0)
print(f"{t.get_celsius()}°C = {t.get_fahrenheit()}°F")

try:
    t.set_celsius(-300)   # Below absolute zero!
except ValueError as err:
    print(f"Validation caught: {err}")


# ---- Example 5: Encapsulating a List ----
# Prevent external code from directly modifying internal collections

class TodoList:
    def __init__(self, name):
        self.__name = name
        self.__tasks = []

    def add_task(self, task):
        if task and task.strip():
            self.__tasks.append(task.strip())
            print(f"Added: '{task.strip()}'")
        else:
            print("Error: Task cannot be empty!")

    def remove_task(self, index):
        if 0 <= index < len(self.__tasks):
            removed = self.__tasks.pop(index)
            print(f"Removed: '{removed}'")
        else:
            print(f"Error: Invalid index {index}")

    def get_tasks(self):
        return self.__tasks.copy()  # Return a COPY, not the original!

    def show(self):
        print(f"\n📋 {self.__name}")
        if not self.__tasks:
            print("  (empty)")
        for i, task in enumerate(self.__tasks):
            print(f"  {i+1}. {task}")

print("\n--- Todo List ---")
todo = TodoList("My Tasks")
todo.add_task("Buy groceries")
todo.add_task("Learn Python OOP")
todo.add_task("")             # Blocked!
todo.show()

# Getting tasks returns a copy - modifying it won't affect the original
tasks_copy = todo.get_tasks()
tasks_copy.append("Hacked task!")
todo.show()  # Original unchanged!


# KEY TAKEAWAYS:
# - Encapsulation bundles data and methods, restricting direct access
# - Python uses CONVENTIONS, not strict enforcement:
#     public (name), protected (_name), private (__name)
# - Private attributes use NAME MANGLING: __attr → _ClassName__attr
# - Use getters/setters to control how attributes are accessed/modified
# - Always validate data in setters
# - Return COPIES of mutable objects (lists, dicts) from getters
# - Next module: @property decorator provides a cleaner way to do this!
