#!/usr/bin/env python

# =============================================================================
# MODULE 06: INHERITANCE - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: School System ----
# Create a hierarchy:
#   - Person: name, age
#   - Student(Person): student_id, grades (list)
#   - Teacher(Person): subject, salary
# Methods:
#   - Student: add_grade(grade), average(), display()
#   - Teacher: give_raise(percent), display()
#
# Expected Output:
# Student: Alice (Age 20) | ID: S001
# Grades: [85, 92, 78, 95] | Average: 87.50
# Teacher: Mr. Smith (Age 35) | Subject: Math
# Salary: $55,000
# After 10% raise: $60,500

# YOUR CODE HERE:




# ---- Question 2: E-Commerce Products ----
# Create a hierarchy:
#   - Product: name, price, weight_kg
#   - DigitalProduct(Product): file_size_mb, download_link (weight=0)
#   - PhysicalProduct(Product): shipping_cost_per_kg
# Methods:
#   - Product: total_price() returns price
#   - DigitalProduct: total_price() returns price (no shipping)
#   - PhysicalProduct: total_price() returns price + (weight * shipping_cost)
#
# Expected Output:
# Python eBook | Price: $29.99 | Total: $29.99
#   Download: 5.2 MB
# Mechanical Keyboard | Price: $89.99 | Total: $95.99
#   Shipping: 0.8 kg × $7.50/kg = $6.00

# YOUR CODE HERE:




# ---- Question 3: Animal Kingdom ----
# Create a hierarchy:
#   - Animal: name, sound, legs
#   - Pet(Animal): owner, vaccinated (bool)
#   - WildAnimal(Animal): habitat, endangered (bool)
# Override __str__ in each class to show relevant info.
#
# Expected Output:
# Pet: Buddy (Dog) | Owner: Alice | Sound: Woof | Legs: 4 | Vaccinated: Yes
# Wild: Simba (Lion) | Habitat: Savanna | Sound: Roar | Legs: 4 | Endangered: Yes
# Is Buddy an Animal? True
# Is Simba a Pet? False

# YOUR CODE HERE:




# ---- Question 4: Bank Account Types ----
# Create a hierarchy:
#   - BankAccount: owner, balance
#   - CheckingAccount(BankAccount): overdraft_limit
#   - SavingsAccount(BankAccount): interest_rate, min_balance
# Override withdraw() in each:
#   - Checking: allow negative balance up to overdraft_limit
#   - Savings: block if would go below min_balance
#
# Expected Output:
# === Checking Account ===
# Alice: $1,000.00 (Overdraft limit: $500)
# Withdrew $800.00. Balance: $200.00
# Withdrew $600.00. Balance: -$400.00
# Overdraft limit exceeded! Max withdrawal: $900.00
# === Savings Account ===
# Bob: $5,000.00 (Min balance: $1,000, Rate: 3.0%)
# Withdrew $3,000.00. Balance: $2,000.00
# Cannot withdraw $1,500.00. Min balance $1,000 required.
# Interest added: $60.00. Balance: $2,060.00

# YOUR CODE HERE:




# ---- Question 5: RPG Character System ----
# Create a hierarchy:
#   - Character: name, health=100, attack=10, defense=5
#   - Warrior(Character): rage=0, attack bonus when rage > 50
#   - Mage(Character): mana=100, can cast spells that cost mana
#   - Healer(Character): heal_power=25, can heal other characters
# Methods:
#   - Character: take_damage(amount), is_alive()
#   - Warrior: battle_cry() increases rage by 25, attack() uses rage bonus
#   - Mage: cast_spell(target) deals 30 damage, costs 20 mana
#   - Healer: heal(target) restores health, costs 15 mana
#
# Expected Output:
# === Battle Arena ===
# Conan (Warrior) HP: 100 | ATK: 15 | DEF: 8 | Rage: 0
# Gandalf (Mage) HP: 100 | ATK: 10 | DEF: 5 | Mana: 100
# Mercy (Healer) HP: 100 | ATK: 8 | DEF: 5 | Mana: 100
# Conan uses Battle Cry! Rage: 25
# Conan uses Battle Cry! Rage: 50
# Conan uses Battle Cry! Rage: 75 (ENRAGED! +10 ATK)
# Gandalf casts spell on Conan! 30 damage! Gandalf's mana: 80
# Conan HP: 70
# Mercy heals Conan for 25 HP! Mercy's mana: 85
# Conan HP: 95

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.grades = []
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def average(self):
#         return sum(self.grades) / len(self.grades) if self.grades else 0
#
#     def display(self):
#         print(f"Student: {self.name} (Age {self.age}) | ID: {self.student_id}")
#         print(f"Grades: {self.grades} | Average: {self.average():.2f}")
#
# class Teacher(Person):
#     def __init__(self, name, age, subject, salary):
#         super().__init__(name, age)
#         self.subject = subject
#         self.salary = salary
#
#     def give_raise(self, percent):
#         self.salary = int(self.salary * (1 + percent / 100))
#
#     def display(self):
#         print(f"Teacher: {self.name} (Age {self.age}) | Subject: {self.subject}")
#         print(f"Salary: ${self.salary:,}")
#
# s = Student("Alice", 20, "S001")
# for g in [85, 92, 78, 95]:
#     s.add_grade(g)
# s.display()
# t = Teacher("Mr. Smith", 35, "Math", 55000)
# t.display()
# t.give_raise(10)
# print(f"After 10% raise: ${t.salary:,}")


# # Question 2:
# class Product:
#     def __init__(self, name, price, weight_kg=0):
#         self.name = name
#         self.price = price
#         self.weight_kg = weight_kg
#
#     def total_price(self):
#         return self.price
#
# class DigitalProduct(Product):
#     def __init__(self, name, price, file_size_mb, download_link=""):
#         super().__init__(name, price, 0)
#         self.file_size_mb = file_size_mb
#         self.download_link = download_link
#
#     def display(self):
#         print(f"{self.name} | Price: ${self.price} | Total: ${self.total_price()}")
#         print(f"  Download: {self.file_size_mb} MB")
#
# class PhysicalProduct(Product):
#     def __init__(self, name, price, weight_kg, shipping_cost_per_kg):
#         super().__init__(name, price, weight_kg)
#         self.shipping_cost_per_kg = shipping_cost_per_kg
#
#     def total_price(self):
#         shipping = self.weight_kg * self.shipping_cost_per_kg
#         return self.price + shipping
#
#     def display(self):
#         shipping = self.weight_kg * self.shipping_cost_per_kg
#         print(f"{self.name} | Price: ${self.price} | Total: ${self.total_price():.2f}")
#         print(f"  Shipping: {self.weight_kg} kg × ${self.shipping_cost_per_kg}/kg = ${shipping:.2f}")
#
# dp = DigitalProduct("Python eBook", 29.99, 5.2)
# dp.display()
# pp = PhysicalProduct("Mechanical Keyboard", 89.99, 0.8, 7.50)
# pp.display()


# # Question 3:
# class Animal:
#     def __init__(self, name, sound, legs):
#         self.name = name
#         self.sound = sound
#         self.legs = legs
#
# class Pet(Animal):
#     def __init__(self, name, sound, legs, owner, vaccinated=True):
#         super().__init__(name, sound, legs)
#         self.owner = owner
#         self.vaccinated = vaccinated
#
#     def __str__(self):
#         vax = "Yes" if self.vaccinated else "No"
#         return f"Pet: {self.name} | Owner: {self.owner} | Sound: {self.sound} | Legs: {self.legs} | Vaccinated: {vax}"
#
# class WildAnimal(Animal):
#     def __init__(self, name, sound, legs, habitat, endangered=False):
#         super().__init__(name, sound, legs)
#         self.habitat = habitat
#         self.endangered = endangered
#
#     def __str__(self):
#         end = "Yes" if self.endangered else "No"
#         return f"Wild: {self.name} | Habitat: {self.habitat} | Sound: {self.sound} | Legs: {self.legs} | Endangered: {end}"
#
# buddy = Pet("Buddy (Dog)", "Woof", 4, "Alice")
# simba = WildAnimal("Simba (Lion)", "Roar", 4, "Savanna", True)
# print(buddy)
# print(simba)
# print(f"Is Buddy an Animal? {isinstance(buddy, Animal)}")
# print(f"Is Simba a Pet? {isinstance(simba, Pet)}")


# # Question 4:
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"Withdrew ${amount:,.2f}. Balance: ${self.balance:,.2f}")
#
# class CheckingAccount(BankAccount):
#     def __init__(self, owner, balance=0, overdraft_limit=500):
#         super().__init__(owner, balance)
#         self.overdraft_limit = overdraft_limit
#
#     def withdraw(self, amount):
#         if self.balance - amount < -self.overdraft_limit:
#             max_w = self.balance + self.overdraft_limit
#             print(f"Overdraft limit exceeded! Max withdrawal: ${max_w:,.2f}")
#         else:
#             self.balance -= amount
#             print(f"Withdrew ${amount:,.2f}. Balance: ${self.balance:,.2f}")
#
#     def display(self):
#         print(f"{self.owner}: ${self.balance:,.2f} (Overdraft limit: ${self.overdraft_limit})")
#
# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance=0, interest_rate=0.03, min_balance=1000):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#         self.min_balance = min_balance
#
#     def withdraw(self, amount):
#         if self.balance - amount < self.min_balance:
#             print(f"Cannot withdraw ${amount:,.2f}. Min balance ${self.min_balance:,} required.")
#         else:
#             self.balance -= amount
#             print(f"Withdrew ${amount:,.2f}. Balance: ${self.balance:,.2f}")
#
#     def add_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         print(f"Interest added: ${interest:,.2f}. Balance: ${self.balance:,.2f}")
#
#     def display(self):
#         print(f"{self.owner}: ${self.balance:,.2f} (Min balance: ${self.min_balance:,}, Rate: {self.interest_rate*100}%)")
#
# print("=== Checking Account ===")
# ca = CheckingAccount("Alice", 1000, 500)
# ca.display()
# ca.withdraw(800)
# ca.withdraw(600)
# ca.withdraw(500)
# print("=== Savings Account ===")
# sa = SavingsAccount("Bob", 5000, 0.03, 1000)
# sa.display()
# sa.withdraw(3000)
# sa.withdraw(1500)
# sa.add_interest()


# # Question 5:
# class Character:
#     def __init__(self, name, health=100, attack=10, defense=5):
#         self.name = name
#         self.health = health
#         self.max_health = health
#         self.attack = attack
#         self.defense = defense
#
#     def take_damage(self, amount):
#         actual = max(0, amount - self.defense)
#         self.health = max(0, self.health - actual)
#
#     def is_alive(self):
#         return self.health > 0
#
# class Warrior(Character):
#     def __init__(self, name, health=100, attack=15, defense=8):
#         super().__init__(name, health, attack, defense)
#         self.rage = 0
#
#     def battle_cry(self):
#         self.rage += 25
#         msg = f"{self.name} uses Battle Cry! Rage: {self.rage}"
#         if self.rage > 50:
#             msg += " (ENRAGED! +10 ATK)"
#         print(msg)
#
#     def status(self):
#         print(f"{self.name} (Warrior) HP: {self.health} | ATK: {self.attack} | DEF: {self.defense} | Rage: {self.rage}")
#
# class Mage(Character):
#     def __init__(self, name, health=100, attack=10, defense=5, mana=100):
#         super().__init__(name, health, attack, defense)
#         self.mana = mana
#
#     def cast_spell(self, target):
#         if self.mana >= 20:
#             self.mana -= 20
#             damage = 30
#             target.health = max(0, target.health - damage)
#             print(f"{self.name} casts spell on {target.name}! {damage} damage! {self.name}'s mana: {self.mana}")
#
#     def status(self):
#         print(f"{self.name} (Mage) HP: {self.health} | ATK: {self.attack} | DEF: {self.defense} | Mana: {self.mana}")
#
# class Healer(Character):
#     def __init__(self, name, health=100, attack=8, defense=5, mana=100):
#         super().__init__(name, health, attack, defense)
#         self.mana = mana
#         self.heal_power = 25
#
#     def heal(self, target):
#         if self.mana >= 15:
#             self.mana -= 15
#             target.health = min(target.max_health, target.health + self.heal_power)
#             print(f"{self.name} heals {target.name} for {self.heal_power} HP! {self.name}'s mana: {self.mana}")
#
#     def status(self):
#         print(f"{self.name} (Healer) HP: {self.health} | ATK: {self.attack} | DEF: {self.defense} | Mana: {self.mana}")
#
# print("=== Battle Arena ===")
# w = Warrior("Conan")
# m = Mage("Gandalf")
# h = Healer("Mercy")
# w.status()
# m.status()
# h.status()
# w.battle_cry()
# w.battle_cry()
# w.battle_cry()
# m.cast_spell(w)
# print(f"{w.name} HP: {w.health}")
# h.heal(w)
# print(f"{w.name} HP: {w.health}")
