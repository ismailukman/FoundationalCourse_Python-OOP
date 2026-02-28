#!/usr/bin/env python

# =============================================================================
# MODULE 05: ENCAPSULATION - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Secure Password Manager ----
# Create a class 'PasswordEntry' with:
#   - Private: __website, __username, __password
#   - Method: get_info() returns website and username (NOT password)
#   - Method: verify_password(attempt) returns True/False
#   - Method: update_password(old_pw, new_pw) changes if old matches
#
# Expected Output:
# Website: gmail.com | User: alice@gmail.com
# Password hidden for security
# Verify 'wrong123': False
# Verify 'secret123': True
# Password updated successfully!
# Verify with new password: True

# YOUR CODE HERE:




# ---- Question 2: Encapsulated Stack ----
# Create a class 'Stack' with:
#   - Private: __items (list), __max_size
#   - Method: push(item) - add if not full
#   - Method: pop() - remove and return top item
#   - Method: peek() - return top item without removing
#   - Method: size() - return current size
#   - Method: is_empty(), is_full()
#
# Expected Output:
# Push: A, B, C
# Size: 3
# Peek: C
# Pop: C
# Pop: B
# Size: 1
# Is empty: False
# Push: D, E, F, G
# Stack is full! Cannot push G
# Size: 5

# YOUR CODE HERE:




# ---- Question 3: Health Tracker ----
# Create a class 'HealthProfile' with:
#   - Private: __name, __weight_kg, __height_m
#   - Protected: _medical_notes (list)
#   - Method: bmi() returns weight / height^2
#   - Method: bmi_category() returns Underweight/Normal/Overweight/Obese
#   - Method: update_weight(new_weight) with validation (30-300 kg)
#   - Method: add_note(note) adds to medical notes
#   - Method: summary() prints full profile
#
# Expected Output:
# Health Profile: John
# Weight: 80.0 kg | Height: 1.75 m
# BMI: 26.12 (Overweight)
# Medical Notes:
#   - Annual checkup: all good
# Updated weight to 72.0 kg
# BMI: 23.51 (Normal)
# Invalid weight: 500 kg rejected

# YOUR CODE HERE:




# ---- Question 4: Encapsulated Scoreboard ----
# Create a class 'Scoreboard' with:
#   - Private: __scores (dict of player: score)
#   - Method: add_player(name) with initial score 0
#   - Method: add_points(name, points) validates positive
#   - Method: get_score(name) returns player's score
#   - Method: get_leader() returns name of player with highest score
#   - Method: get_rankings() returns sorted list of (name, score) tuples
#   - Method: display() prints formatted scoreboard
#
# Expected Output:
# === SCOREBOARD ===
#  1. Charlie: 45 pts
#  2. Alice: 35 pts
#  3. Bob: 20 pts
# Leader: Charlie
# Alice's score: 35

# YOUR CODE HERE:




# ---- Question 5: Secure Diary ----
# Create a class 'Diary' with:
#   - Private: __entries (list of dicts with date and content)
#   - Private: __pin (4-digit string)
#   - Method: write(pin, content) adds entry if pin correct
#   - Method: read_all(pin) returns all entries if pin correct
#   - Method: read_latest(pin) returns last entry
#   - Method: change_pin(old_pin, new_pin) updates pin
#   - Method: entry_count() returns number of entries (no pin needed)
#
# Expected Output:
# Entry added: 2025-01-15
# Entry added: 2025-01-16
# Wrong PIN! Access denied.
# --- All Entries ---
# [2025-01-15] Had a great day learning Python!
# [2025-01-16] Encapsulation is fascinating!
# Total entries: 2
# PIN changed successfully!

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# class PasswordEntry:
#     def __init__(self, website, username, password):
#         self.__website = website
#         self.__username = username
#         self.__password = password
#
#     def get_info(self):
#         print(f"Website: {self.__website} | User: {self.__username}")
#         print("Password hidden for security")
#
#     def verify_password(self, attempt):
#         return attempt == self.__password
#
#     def update_password(self, old_pw, new_pw):
#         if self.verify_password(old_pw):
#             self.__password = new_pw
#             print("Password updated successfully!")
#             return True
#         print("Wrong password!")
#         return False
#
# entry = PasswordEntry("gmail.com", "alice@gmail.com", "secret123")
# entry.get_info()
# print(f"Verify 'wrong123': {entry.verify_password('wrong123')}")
# print(f"Verify 'secret123': {entry.verify_password('secret123')}")
# entry.update_password("secret123", "newpass456")
# print(f"Verify with new password: {entry.verify_password('newpass456')}")


# # Question 2:
# class Stack:
#     def __init__(self, max_size=5):
#         self.__items = []
#         self.__max_size = max_size
#
#     def push(self, item):
#         if self.is_full():
#             print(f"Stack is full! Cannot push {item}")
#             return
#         self.__items.append(item)
#
#     def pop(self):
#         if self.is_empty():
#             print("Stack is empty!")
#             return None
#         return self.__items.pop()
#
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.__items[-1]
#
#     def size(self):
#         return len(self.__items)
#
#     def is_empty(self):
#         return len(self.__items) == 0
#
#     def is_full(self):
#         return len(self.__items) >= self.__max_size
#
# s = Stack(5)
# print("Push: A, B, C")
# for item in ["A", "B", "C"]:
#     s.push(item)
# print(f"Size: {s.size()}")
# print(f"Peek: {s.peek()}")
# print(f"Pop: {s.pop()}")
# print(f"Pop: {s.pop()}")
# print(f"Size: {s.size()}")
# print(f"Is empty: {s.is_empty()}")
# print("Push: D, E, F, G")
# for item in ["D", "E", "F", "G"]:
#     s.push(item)
# print(f"Size: {s.size()}")


# # Question 3:
# class HealthProfile:
#     def __init__(self, name, weight_kg, height_m):
#         self.__name = name
#         self.__weight_kg = weight_kg
#         self.__height_m = height_m
#         self._medical_notes = []
#
#     def bmi(self):
#         return self.__weight_kg / (self.__height_m ** 2)
#
#     def bmi_category(self):
#         b = self.bmi()
#         if b < 18.5: return "Underweight"
#         elif b < 25: return "Normal"
#         elif b < 30: return "Overweight"
#         else: return "Obese"
#
#     def update_weight(self, new_weight):
#         if 30 <= new_weight <= 300:
#             self.__weight_kg = new_weight
#             print(f"Updated weight to {new_weight} kg")
#         else:
#             print(f"Invalid weight: {new_weight} kg rejected")
#
#     def add_note(self, note):
#         self._medical_notes.append(note)
#
#     def summary(self):
#         print(f"Health Profile: {self.__name}")
#         print(f"Weight: {self.__weight_kg} kg | Height: {self.__height_m} m")
#         print(f"BMI: {self.bmi():.2f} ({self.bmi_category()})")
#         if self._medical_notes:
#             print("Medical Notes:")
#             for note in self._medical_notes:
#                 print(f"  - {note}")
#
# hp = HealthProfile("John", 80, 1.75)
# hp.add_note("Annual checkup: all good")
# hp.summary()
# hp.update_weight(72)
# print(f"BMI: {hp.bmi():.2f} ({hp.bmi_category()})")
# hp.update_weight(500)


# # Question 4:
# class Scoreboard:
#     def __init__(self):
#         self.__scores = {}
#
#     def add_player(self, name):
#         self.__scores[name] = 0
#
#     def add_points(self, name, points):
#         if points > 0 and name in self.__scores:
#             self.__scores[name] += points
#
#     def get_score(self, name):
#         return self.__scores.get(name, 0)
#
#     def get_leader(self):
#         return max(self.__scores, key=self.__scores.get)
#
#     def get_rankings(self):
#         return sorted(self.__scores.items(), key=lambda x: x[1], reverse=True)
#
#     def display(self):
#         print("=== SCOREBOARD ===")
#         for i, (name, score) in enumerate(self.get_rankings(), 1):
#             print(f" {i}. {name}: {score} pts")
#
# sb = Scoreboard()
# sb.add_player("Alice")
# sb.add_player("Bob")
# sb.add_player("Charlie")
# sb.add_points("Alice", 35)
# sb.add_points("Bob", 20)
# sb.add_points("Charlie", 45)
# sb.display()
# print(f"Leader: {sb.get_leader()}")
# print(f"Alice's score: {sb.get_score('Alice')}")


# # Question 5:
# from datetime import date
# class Diary:
#     def __init__(self, pin):
#         self.__entries = []
#         self.__pin = pin
#
#     def __verify_pin(self, pin):
#         return pin == self.__pin
#
#     def write(self, pin, content, entry_date=None):
#         if not self.__verify_pin(pin):
#             print("Wrong PIN! Access denied.")
#             return
#         d = entry_date or str(date.today())
#         self.__entries.append({"date": d, "content": content})
#         print(f"Entry added: {d}")
#
#     def read_all(self, pin):
#         if not self.__verify_pin(pin):
#             print("Wrong PIN! Access denied.")
#             return
#         print("--- All Entries ---")
#         for e in self.__entries:
#             print(f"[{e['date']}] {e['content']}")
#
#     def read_latest(self, pin):
#         if not self.__verify_pin(pin):
#             print("Wrong PIN! Access denied.")
#             return None
#         return self.__entries[-1] if self.__entries else None
#
#     def change_pin(self, old_pin, new_pin):
#         if self.__verify_pin(old_pin):
#             self.__pin = new_pin
#             print("PIN changed successfully!")
#         else:
#             print("Wrong PIN!")
#
#     def entry_count(self):
#         return len(self.__entries)
#
# d = Diary("1234")
# d.write("1234", "Had a great day learning Python!", "2025-01-15")
# d.write("1234", "Encapsulation is fascinating!", "2025-01-16")
# d.write("0000", "Try to hack!")
# d.read_all("1234")
# print(f"Total entries: {d.entry_count()}")
# d.change_pin("1234", "5678")
