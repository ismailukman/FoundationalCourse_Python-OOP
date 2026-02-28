#!/usr/bin/env python

# =============================================================================
# MODULE 03: CLASS VARIABLES vs INSTANCE VARIABLES - EXERCISES
# =============================================================================
# Test your understanding of class vs instance variables.
# =============================================================================


# ---- Exercise 1: Identify the Variable Types ----
# In the class below, identify which are class variables and which are
# instance variables. Write your answers as comments.

class School:
    school_name = "Springfield High"        # ??? variable
    max_students = 500                      # ??? variable

    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name    # ??? variable
        self.subject = subject              # ??? variable
        self.students = []                  # ??? variable


# ---- Exercise 2: Employee Counter ----
# Create a class 'Worker' with:
#   - Class variable: worker_count (starts at 0)
#   - Instance variables: name, role
#   - __init__ should increment worker_count
# Create 3 workers and print the total count.

# YOUR CODE HERE:




# ---- Exercise 3: Shared Configuration ----
# Create a class 'AppConfig' with:
#   - Class variables: version = "1.0", debug = False, max_retries = 3
#   - Instance variables: app_name, port
#   - Method: show_config() prints all config including class variables
# Create two apps and show how changing a class variable affects both.

# YOUR CODE HERE:




# ---- Exercise 4: Predict the Output ----
# What will each print statement output? Write your predictions.

class Tracker:
    count = 0
    items = []

    def __init__(self, name):
        self.name = name
        Tracker.count += 1
        Tracker.items.append(name)

t1 = Tracker("Alpha")
t2 = Tracker("Beta")
t3 = Tracker("Gamma")

# Prediction: ___
print(t1.count)

# Prediction: ___
print(Tracker.count)

# Prediction: ___
print(t2.items)

t1.count = 100    # What does this do?

# Prediction: ___
print(t1.count)

# Prediction: ___
print(t2.count)

# Prediction: ___
print(Tracker.count)


# ---- Exercise 5: Fix the Bug ----
# This code has a bug with class variables. Find and fix it.

class ChatRoom:
    messages = []    # Intended to be unique per room, but it's shared!

    def __init__(self, room_name):
        self.room_name = room_name

    def send(self, msg):
        self.messages.append(f"[{self.room_name}] {msg}")

    def show(self):
        for m in self.messages:
            print(m)

# Uncomment to see the bug:
# room1 = ChatRoom("General")
# room2 = ChatRoom("Random")
# room1.send("Hello!")
# room2.send("Hey there!")
# print("Room 1 messages:")
# room1.show()    # Shows BOTH messages! Bug!

# YOUR FIX HERE:




# =============================================================================
# HINTS
# =============================================================================
# Exercise 1: school_name and max_students = class variables
#             teacher_name, subject, students = instance variables
#
# Exercise 2: Use Worker.worker_count += 1 in __init__
#
# Exercise 3: Change class var with AppConfig.debug = True
#
# Exercise 4: t1.count=3, Tracker.count=3, t2.items=['Alpha','Beta','Gamma'],
#             After t1.count=100: t1.count=100, t2.count=3, Tracker.count=3
#             (t1.count = 100 creates an INSTANCE variable on t1)
#
# Exercise 5: Move messages=[] into __init__ as self.messages = []
# =============================================================================
