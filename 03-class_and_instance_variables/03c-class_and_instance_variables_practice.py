#!/usr/bin/env python

# =============================================================================
# MODULE 03: CLASS VARIABLES vs INSTANCE VARIABLES - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Library System ----
# Create a class 'LibraryBook' with:
#   - Class variables: total_books = 0, all_books = []
#   - Instance variables: title, author, is_available (default True)
#   - Methods: borrow(), return_book()
#   - Class should track total books created
#
# Expected Output:
# Total books in library: 3
# All books: Harry Potter, 1984, The Hobbit
# Borrowing 'Harry Potter'... Success!
# Borrowing 'Harry Potter'... Already borrowed!
# Returning 'Harry Potter'... Success!
# Available: Harry Potter: Yes | 1984: Yes | The Hobbit: Yes

# YOUR CODE HERE:




# ---- Question 2: Game Character ----
# Create a class 'GameCharacter' with:
#   - Class variables: max_health = 100, characters_created = 0
#   - Instance variables: name, health (starts at max_health), level (default=1)
#   - Method: take_damage(amount) - reduce health (min 0)
#   - Method: heal(amount) - increase health (max = max_health)
#   - Method: status() - display character info
#
# Expected Output:
# Characters created: 2
# Warrior (Lv.1) | HP: 100/100
# Mage (Lv.3) | HP: 100/100
# Warrior takes 30 damage!
# Warrior (Lv.1) | HP: 70/100
# Warrior heals 15!
# Warrior (Lv.1) | HP: 85/100
# Warrior takes 200 damage!
# Warrior (Lv.1) | HP: 0/100

# YOUR CODE HERE:




# ---- Question 3: Currency Converter ----
# Create a class 'Money' with:
#   - Class variable: exchange_rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.73, "JPY": 110.0}
#   - Instance variables: amount, currency
#   - Method: convert_to(target_currency) -> returns new Money object
#   - Method: display() -> prints formatted amount
#
# Expected Output:
# $100.00 USD
# €85.00 EUR
# £73.00 GBP
# ¥11000.00 JPY

# YOUR CODE HERE:




# ---- Question 4: Class Roster ----
# Create a class 'ClassRoster' with:
#   - Class variable: max_class_size = 30
#   - Instance variables: class_name, teacher, students (list)
#   - Method: add_student(name) - add if not full
#   - Method: remove_student(name) - remove if exists
#   - Method: is_full() - returns True if at max
#   - Method: roster() - prints formatted roster
#
# Expected Output:
# === Math 101 (Ms. Johnson) ===
# Max class size: 30
# Enrolled: 3/30
# 1. Alice
# 2. Bob
# 3. Charlie
# Removing Bob...
# Enrolled: 2/30
# 1. Alice
# 2. Charlie

# YOUR CODE HERE:




# ---- Question 5: Config Manager ----
# Create a class 'DatabaseConfig' with:
#   - Class variables: host="localhost", port=5432, max_connections=10,
#                      connection_count=0
#   - Instance variables: db_name, username
#   - Method: connect() -> increments connection_count (if under max)
#   - Method: disconnect() -> decrements connection_count
#   - Class method alternative: show_config() prints all shared settings
#
# Expected Output:
# Config: localhost:5432 | Max Connections: 10
# DB1 connected. Active connections: 1
# DB2 connected. Active connections: 2
# DB1 connected again. Active connections: 3
# DB2 disconnected. Active connections: 2
# DB1 connects: Active connections: 3

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# class LibraryBook:
#     total_books = 0
#     all_books = []
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_available = True
#         LibraryBook.total_books += 1
#         LibraryBook.all_books.append(self)
#
#     def borrow(self):
#         if self.is_available:
#             self.is_available = False
#             print(f"Borrowing '{self.title}'... Success!")
#         else:
#             print(f"Borrowing '{self.title}'... Already borrowed!")
#
#     def return_book(self):
#         self.is_available = True
#         print(f"Returning '{self.title}'... Success!")
#
# b1 = LibraryBook("Harry Potter", "J.K. Rowling")
# b2 = LibraryBook("1984", "George Orwell")
# b3 = LibraryBook("The Hobbit", "J.R.R. Tolkien")
# print(f"Total books in library: {LibraryBook.total_books}")
# print(f"All books: {', '.join(b.title for b in LibraryBook.all_books)}")
# b1.borrow()
# b1.borrow()
# b1.return_book()
# avail = " | ".join(f"{b.title}: {'Yes' if b.is_available else 'No'}" for b in LibraryBook.all_books)
# print(f"Available: {avail}")


# # Question 2:
# class GameCharacter:
#     max_health = 100
#     characters_created = 0
#
#     def __init__(self, name, level=1):
#         self.name = name
#         self.health = GameCharacter.max_health
#         self.level = level
#         GameCharacter.characters_created += 1
#
#     def take_damage(self, amount):
#         self.health = max(0, self.health - amount)
#         print(f"{self.name} takes {amount} damage!")
#
#     def heal(self, amount):
#         self.health = min(GameCharacter.max_health, self.health + amount)
#         print(f"{self.name} heals {amount}!")
#
#     def status(self):
#         print(f"{self.name} (Lv.{self.level}) | HP: {self.health}/{GameCharacter.max_health}")
#
# c1 = GameCharacter("Warrior")
# c2 = GameCharacter("Mage", 3)
# print(f"Characters created: {GameCharacter.characters_created}")
# c1.status()
# c2.status()
# c1.take_damage(30)
# c1.status()
# c1.heal(15)
# c1.status()
# c1.take_damage(200)
# c1.status()


# # Question 3:
# class Money:
#     exchange_rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.73, "JPY": 110.0}
#     symbols = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥"}
#
#     def __init__(self, amount, currency="USD"):
#         self.amount = amount
#         self.currency = currency
#
#     def convert_to(self, target_currency):
#         usd_amount = self.amount / Money.exchange_rates[self.currency]
#         target_amount = usd_amount * Money.exchange_rates[target_currency]
#         return Money(target_amount, target_currency)
#
#     def display(self):
#         symbol = Money.symbols.get(self.currency, "")
#         print(f"{symbol}{self.amount:.2f} {self.currency}")
#
# m = Money(100, "USD")
# m.display()
# m.convert_to("EUR").display()
# m.convert_to("GBP").display()
# m.convert_to("JPY").display()


# # Question 4:
# class ClassRoster:
#     max_class_size = 30
#
#     def __init__(self, class_name, teacher):
#         self.class_name = class_name
#         self.teacher = teacher
#         self.students = []
#
#     def add_student(self, name):
#         if not self.is_full():
#             self.students.append(name)
#         else:
#             print(f"Class is full! Cannot add {name}")
#
#     def remove_student(self, name):
#         if name in self.students:
#             self.students.remove(name)
#             print(f"Removing {name}...")
#
#     def is_full(self):
#         return len(self.students) >= ClassRoster.max_class_size
#
#     def roster(self):
#         print(f"=== {self.class_name} ({self.teacher}) ===")
#         print(f"Max class size: {ClassRoster.max_class_size}")
#         print(f"Enrolled: {len(self.students)}/{ClassRoster.max_class_size}")
#         for i, s in enumerate(self.students, 1):
#             print(f"{i}. {s}")
#
# r = ClassRoster("Math 101", "Ms. Johnson")
# r.add_student("Alice")
# r.add_student("Bob")
# r.add_student("Charlie")
# r.roster()
# r.remove_student("Bob")
# print(f"Enrolled: {len(r.students)}/{ClassRoster.max_class_size}")
# for i, s in enumerate(r.students, 1):
#     print(f"{i}. {s}")


# # Question 5:
# class DatabaseConfig:
#     host = "localhost"
#     port = 5432
#     max_connections = 10
#     connection_count = 0
#
#     def __init__(self, db_name, username):
#         self.db_name = db_name
#         self.username = username
#
#     def connect(self):
#         if DatabaseConfig.connection_count < DatabaseConfig.max_connections:
#             DatabaseConfig.connection_count += 1
#             print(f"{self.db_name} connected. Active connections: {DatabaseConfig.connection_count}")
#         else:
#             print("Max connections reached!")
#
#     def disconnect(self):
#         if DatabaseConfig.connection_count > 0:
#             DatabaseConfig.connection_count -= 1
#             print(f"{self.db_name} disconnected. Active connections: {DatabaseConfig.connection_count}")
#
#     @staticmethod
#     def show_config():
#         print(f"Config: {DatabaseConfig.host}:{DatabaseConfig.port} | Max Connections: {DatabaseConfig.max_connections}")
#
# DatabaseConfig.show_config()
# db1 = DatabaseConfig("DB1", "admin")
# db2 = DatabaseConfig("DB2", "user")
# db1.connect()
# db2.connect()
# db1.connect()
# db2.disconnect()
# db1.connect()
