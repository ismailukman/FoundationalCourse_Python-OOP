#!/usr/bin/env python

# =============================================================================
# MODULE 10: ABSTRACT CLASSES AND DESIGN PATTERNS - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Plugin System with Abstract Base ----
# Create an abstract 'Plugin' class and a 'PluginManager' that:
#   - Plugin ABC has: name (abstract property), execute(data) (abstract)
#   - PluginManager: register(plugin), unregister(name), run_all(data)
#   - Create 3 concrete plugins: UpperPlugin, ReversePlugin, CountPlugin
#
# Expected Output:
# Registered: Upper
# Registered: Reverse
# Registered: Counter
# Running 3 plugins on "Hello World":
#   [Upper] HELLO WORLD
#   [Reverse] dlroW olleH
#   [Counter] 11 characters
# Unregistered: Reverse
# Running 2 plugins on "Python OOP":
#   [Upper] PYTHON OOP
#   [Counter] 10 characters

# YOUR CODE HERE:




# ---- Question 2: MRO and super() Chain ----
# Create a class hierarchy that demonstrates cooperative multiple inheritance
# using super(). Each class's __init__ should print when called and pass
# remaining kwargs up the chain.
#
# Classes: Base, Logger(Base), Serializer(Base), Validator(Base)
# Combined: SuperModel(Logger, Serializer, Validator)
#
# Expected Output:
# Creating SuperModel...
# Logger.__init__ called
# Serializer.__init__ called
# Validator.__init__ called
# Base.__init__ called
# MRO: SuperModel -> Logger -> Serializer -> Validator -> Base -> object
# SuperModel has: log, serialize, validate methods

# YOUR CODE HERE:




# ---- Question 3: Complete Composition System ----
# Build a 'NotificationService' using composition:
#   - MessageFormatter (formats message): format(msg) -> str
#   - Sender ABC with concrete: EmailSender, SMSSender, PushSender
#   - Logger: logs every action
#   - NotificationService: HAS formatter, sender, logger
#
# Expected Output:
# [LOG] Service initialised with EmailSender
# [LOG] Formatting message: Welcome!
# [LOG] Sending via Email: *** Welcome! ***
# [EMAIL] Sent: *** Welcome! ***
# ---
# [LOG] Service initialised with SMSSender
# [LOG] Formatting message: Alert!
# [LOG] Sending via SMS: *** Alert! ***
# [SMS] Sent: *** Alert! ***

# YOUR CODE HERE:




# ---- Question 4: Observer Pattern — Event System ----
# Build a complete event system:
#   - EventBus: register(event, handler), unregister(event, handler), emit(event, **data)
#   - UserService: emits "user_created", "user_deleted" events
#   - Create handlers: log_handler, email_handler, analytics_handler
#
# Expected Output:
# [ANALYTICS] Event: user_created | Data: {'name': 'Alice', 'email': 'alice@test.com'}
# [LOG] Event: user_created | User: Alice
# [EMAIL] Welcome email sent to alice@test.com
# [ANALYTICS] Event: user_created | Data: {'name': 'Bob', 'email': 'bob@test.com'}
# [LOG] Event: user_created | User: Bob
# [EMAIL] Welcome email sent to bob@test.com
# Removing email handler...
# [ANALYTICS] Event: user_deleted | Data: {'name': 'Alice'}
# [LOG] Event: user_deleted | User: Alice

# YOUR CODE HERE:




# ---- Question 5: Full OOP Project — Library Management System ----
# Build a mini library system using ALL OOP concepts from the course:
#   - Abstract class: LibraryItem (title, item_id, is_available)
#   - Concrete: Book(author, pages), DVD(director, duration), Magazine(issue)
#   - Mixin: SearchableMixin (matches(query) checks title)
#   - Composition: Library HAS-A list of items and a Catalogue
#   - Catalogue: search(query), filter_by_type(item_type)
#   - Library: add_item, remove_item, checkout(item_id), return_item(item_id)
#   - Use @property for is_available and item counts
#
# Expected Output:
# === Library System ===
# Added: Book 'Python OOP' by Guido
# Added: Book 'Clean Code' by Martin
# Added: DVD 'Python Tutorial' by Tech Co (120 min)
# Added: Magazine 'PyMag Issue #42'
#
# Total items: 4 | Available: 4
#
# Search 'python':
#   [Book] Python OOP by Guido - Available
#   [DVD] Python Tutorial (120 min) - Available
#
# Checkout 'Python OOP'... Success!
# Total items: 4 | Available: 3
#
# Checkout 'Python OOP'... Error: Item not available
#
# Return 'Python OOP'... Success!
# Total items: 4 | Available: 4
#
# Books only:
#   [Book] Python OOP by Guido - Available
#   [Book] Clean Code by Martin - Available

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# from abc import ABC, abstractmethod
#
# class Plugin(ABC):
#     @property
#     @abstractmethod
#     def name(self):
#         pass
#
#     @abstractmethod
#     def execute(self, data):
#         pass
#
# class UpperPlugin(Plugin):
#     @property
#     def name(self):
#         return "Upper"
#     def execute(self, data):
#         return data.upper()
#
# class ReversePlugin(Plugin):
#     @property
#     def name(self):
#         return "Reverse"
#     def execute(self, data):
#         return data[::-1]
#
# class CountPlugin(Plugin):
#     @property
#     def name(self):
#         return "Counter"
#     def execute(self, data):
#         return f"{len(data)} characters"
#
# class PluginManager:
#     def __init__(self):
#         self._plugins = {}
#
#     def register(self, plugin):
#         if not isinstance(plugin, Plugin):
#             raise TypeError("Must be a Plugin subclass")
#         self._plugins[plugin.name] = plugin
#         print(f"Registered: {plugin.name}")
#
#     def unregister(self, name):
#         if name in self._plugins:
#             del self._plugins[name]
#             print(f"Unregistered: {name}")
#
#     def run_all(self, data):
#         print(f'Running {len(self._plugins)} plugins on "{data}":')
#         for name, plugin in self._plugins.items():
#             result = plugin.execute(data)
#             print(f"  [{name}] {result}")
#
# pm = PluginManager()
# pm.register(UpperPlugin())
# pm.register(ReversePlugin())
# pm.register(CountPlugin())
# pm.run_all("Hello World")
# pm.unregister("Reverse")
# pm.run_all("Python OOP")


# # Question 2:
# class Base:
#     def __init__(self, **kwargs):
#         print("Base.__init__ called")
#         super().__init__(**kwargs)
#
# class Logger(Base):
#     def __init__(self, **kwargs):
#         print("Logger.__init__ called")
#         super().__init__(**kwargs)
#     def log(self, msg):
#         print(f"[LOG] {msg}")
#
# class Serializer(Base):
#     def __init__(self, **kwargs):
#         print("Serializer.__init__ called")
#         super().__init__(**kwargs)
#     def serialize(self):
#         return str(self.__dict__)
#
# class Validator(Base):
#     def __init__(self, **kwargs):
#         print("Validator.__init__ called")
#         super().__init__(**kwargs)
#     def validate(self):
#         return True
#
# class SuperModel(Logger, Serializer, Validator):
#     def __init__(self, **kwargs):
#         print("Creating SuperModel...")
#         super().__init__(**kwargs)
#
# sm = SuperModel()
# mro_names = [cls.__name__ for cls in SuperModel.__mro__]
# print(f"MRO: {' -> '.join(mro_names)}")
# methods = []
# if hasattr(sm, 'log'): methods.append('log')
# if hasattr(sm, 'serialize'): methods.append('serialize')
# if hasattr(sm, 'validate'): methods.append('validate')
# print(f"SuperModel has: {', '.join(methods)} methods")


# # Question 3:
# from abc import ABC, abstractmethod
#
# class Logger:
#     def log(self, message):
#         print(f"[LOG] {message}")
#
# class MessageFormatter:
#     def format(self, message):
#         return f"*** {message} ***"
#
# class Sender(ABC):
#     @property
#     @abstractmethod
#     def name(self):
#         pass
#
#     @abstractmethod
#     def send(self, message):
#         pass
#
# class EmailSender(Sender):
#     @property
#     def name(self):
#         return "EmailSender"
#     def send(self, message):
#         print(f"[EMAIL] Sent: {message}")
#
# class SMSSender(Sender):
#     @property
#     def name(self):
#         return "SMSSender"
#     def send(self, message):
#         print(f"[SMS] Sent: {message}")
#
# class PushSender(Sender):
#     @property
#     def name(self):
#         return "PushSender"
#     def send(self, message):
#         print(f"[PUSH] Sent: {message}")
#
# class NotificationService:
#     def __init__(self, sender):
#         self.formatter = MessageFormatter()
#         self.sender = sender
#         self.logger = Logger()
#         self.logger.log(f"Service initialised with {sender.name}")
#
#     def notify(self, message):
#         self.logger.log(f"Formatting message: {message}")
#         formatted = self.formatter.format(message)
#         self.logger.log(f"Sending via {self.sender.name.replace('Sender', '')}: {formatted}")
#         self.sender.send(formatted)
#
# email_service = NotificationService(EmailSender())
# email_service.notify("Welcome!")
# print("---")
# sms_service = NotificationService(SMSSender())
# sms_service.notify("Alert!")


# # Question 4:
# class EventBus:
#     def __init__(self):
#         self._handlers = {}
#
#     def register(self, event, handler):
#         if event not in self._handlers:
#             self._handlers[event] = []
#         self._handlers[event].append(handler)
#
#     def unregister(self, event, handler):
#         if event in self._handlers:
#             self._handlers[event].remove(handler)
#
#     def emit(self, event, **data):
#         for handler in self._handlers.get(event, []):
#             handler(event, data)
#
# def analytics_handler(event, data):
#     print(f"[ANALYTICS] Event: {event} | Data: {data}")
#
# def log_handler(event, data):
#     name = data.get("name", "Unknown")
#     print(f"[LOG] Event: {event} | User: {name}")
#
# def email_handler(event, data):
#     email = data.get("email", "")
#     if email:
#         print(f"[EMAIL] Welcome email sent to {email}")
#
# class UserService:
#     def __init__(self, bus):
#         self.bus = bus
#
#     def create_user(self, name, email):
#         self.bus.emit("user_created", name=name, email=email)
#
#     def delete_user(self, name):
#         self.bus.emit("user_deleted", name=name)
#
# bus = EventBus()
# bus.register("user_created", analytics_handler)
# bus.register("user_created", log_handler)
# bus.register("user_created", email_handler)
# bus.register("user_deleted", analytics_handler)
# bus.register("user_deleted", log_handler)
#
# service = UserService(bus)
# service.create_user("Alice", "alice@test.com")
# service.create_user("Bob", "bob@test.com")
# print("Removing email handler...")
# bus.unregister("user_created", email_handler)
# service.delete_user("Alice")


# # Question 5:
# from abc import ABC, abstractmethod
#
# class SearchableMixin:
#     def matches(self, query):
#         return query.lower() in self.title.lower()
#
# class LibraryItem(ABC):
#     def __init__(self, item_id, title):
#         self.item_id = item_id
#         self.title = title
#         self._is_available = True
#
#     @property
#     def is_available(self):
#         return self._is_available
#
#     @is_available.setter
#     def is_available(self, value):
#         self._is_available = value
#
#     @abstractmethod
#     def display(self):
#         pass
#
# class Book(SearchableMixin, LibraryItem):
#     def __init__(self, item_id, title, author, pages):
#         super().__init__(item_id, title)
#         self.author = author
#         self.pages = pages
#
#     def display(self):
#         status = "Available" if self.is_available else "Checked Out"
#         return f"[Book] {self.title} by {self.author} - {status}"
#
# class DVD(SearchableMixin, LibraryItem):
#     def __init__(self, item_id, title, director, duration):
#         super().__init__(item_id, title)
#         self.director = director
#         self.duration = duration
#
#     def display(self):
#         status = "Available" if self.is_available else "Checked Out"
#         return f"[DVD] {self.title} ({self.duration} min) - {status}"
#
# class Magazine(SearchableMixin, LibraryItem):
#     def __init__(self, item_id, title, issue):
#         super().__init__(item_id, title)
#         self.issue = issue
#
#     def display(self):
#         status = "Available" if self.is_available else "Checked Out"
#         return f"[Magazine] {self.title} Issue #{self.issue} - {status}"
#
# class Catalogue:
#     def __init__(self, items):
#         self._items = items
#
#     def search(self, query):
#         return [item for item in self._items if item.matches(query)]
#
#     def filter_by_type(self, item_type):
#         return [item for item in self._items if isinstance(item, item_type)]
#
# class Library:
#     def __init__(self):
#         self._items = {}
#         self.catalogue = Catalogue(self._items)
#
#     def add_item(self, item):
#         self._items[item.item_id] = item
#         print(f"Added: {item.display()}")
#
#     def remove_item(self, item_id):
#         if item_id in self._items:
#             del self._items[item_id]
#
#     @property
#     def total_items(self):
#         return len(self._items)
#
#     @property
#     def available_items(self):
#         return sum(1 for item in self._items.values() if item.is_available)
#
#     def status(self):
#         print(f"Total items: {self.total_items} | Available: {self.available_items}")
#
#     def checkout(self, title):
#         for item in self._items.values():
#             if item.title == title:
#                 if item.is_available:
#                     item.is_available = False
#                     print(f"Checkout '{title}'... Success!")
#                     return True
#                 else:
#                     print(f"Checkout '{title}'... Error: Item not available")
#                     return False
#         print(f"Checkout '{title}'... Error: Item not found")
#         return False
#
#     def return_item(self, title):
#         for item in self._items.values():
#             if item.title == title:
#                 item.is_available = True
#                 print(f"Return '{title}'... Success!")
#                 return True
#         return False
#
# print("=== Library System ===")
# lib = Library()
# lib.add_item(Book("B1", "Python OOP", "Guido", 350))
# lib.add_item(Book("B2", "Clean Code", "Martin", 464))
# lib.add_item(DVD("D1", "Python Tutorial", "Tech Co", 120))
# lib.add_item(Magazine("M1", "PyMag", 42))
# print()
# lib.status()
# print()
#
# results = lib.catalogue.search("python")
# print("Search 'python':")
# for item in results:
#     print(f"  {item.display()}")
# print()
#
# lib.checkout("Python OOP")
# lib.status()
# print()
#
# lib.checkout("Python OOP")
# print()
#
# lib.return_item("Python OOP")
# lib.status()
# print()
#
# books = lib.catalogue.filter_by_type(Book)
# print("Books only:")
# for book in books:
#     print(f"  {book.display()}")
