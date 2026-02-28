#!/usr/bin/env python

# =============================================================================
# MODULE 02: THE __init__ CONSTRUCTOR - PRACTICAL QUESTIONS
# =============================================================================
# Solve each problem. Expected output is provided for verification.
# =============================================================================


# ---- Question 1: Student Enrolment ----
# Create a class 'Student' with:
#   - Attributes: name, student_id, courses (empty list by default)
#   - Method: enrol(course_name) -> adds course to list
#   - Method: drop(course_name) -> removes course if exists
#   - Method: show_courses() -> prints all enrolled courses
#
# Expected Output:
# Student: Alice (ID: S001)
# Enrolled in: Math, Science, English
# After dropping Science:
# Enrolled in: Math, English

# YOUR CODE HERE:




# ---- Question 2: Time Class ----
# Create a class 'Time' with:
#   - __init__ takes hours, minutes, seconds (all default to 0)
#   - Validate: hours (0-23), minutes (0-59), seconds (0-59)
#   - Method: total_seconds() -> converts to total seconds
#   - Method: display() -> prints in HH:MM:SS format
#   - Derived attribute: period -> "AM" or "PM" based on hours
#
# Expected Output:
# 14:30:45 PM
# Total seconds: 52245
# 09:15:00 AM
# Total seconds: 33300

# YOUR CODE HERE:




# ---- Question 3: Product Inventory ----
# Create a class 'Product' with:
#   - Attributes: name, price, stock (default=0)
#   - Method: restock(quantity) -> adds to stock
#   - Method: sell(quantity) -> reduces stock if enough, else prints warning
#   - Method: revenue(quantity) -> returns price * quantity (potential revenue)
#   - Method: info() -> prints product info
#
# Expected Output:
# Product: Widget | Price: $9.99 | Stock: 0
# Restocked 100 units. Stock: 100
# Sold 30 units. Stock: 70
# Cannot sell 80 units. Only 70 in stock.
# Potential revenue for 50 units: $499.50

# YOUR CODE HERE:




# ---- Question 4: Email Builder ----
# Create a class 'Email' with:
#   - __init__ takes: sender, recipient, subject (default="No Subject")
#   - Attributes: body (empty string), attachments (empty list)
#   - Method: write(text) -> sets the body
#   - Method: attach(filename) -> adds to attachments list
#   - Method: preview() -> prints formatted email preview
#
# Expected Output:
# ===== EMAIL PREVIEW =====
# From: alice@mail.com
# To: bob@mail.com
# Subject: Meeting Tomorrow
# Attachments: agenda.pdf, notes.docx
# ---
# Hi Bob, let's meet at 3pm to discuss the project.
# =========================

# YOUR CODE HERE:




# ---- Question 5: Quiz Score Tracker ----
# Create a class 'QuizTracker' with:
#   - __init__ takes: student_name, total_questions
#   - Attributes: correct (0), incorrect (0), unanswered (= total_questions)
#   - Method: answer(is_correct) -> updates counts (bool parameter)
#   - Method: score_percentage() -> returns (correct / total) * 100
#   - Method: summary() -> prints full summary
#
# Expected Output:
# Quiz Summary for Charlie
# Total Questions: 10
# Correct: 7 | Incorrect: 2 | Unanswered: 1
# Score: 70.00%
# Result: PASS

# YOUR CODE HERE:




# =============================================================================
# SOLUTIONS
# =============================================================================

# # Question 1:
# class Student:
#     def __init__(self, name, student_id, courses=None):
#         self.name = name
#         self.student_id = student_id
#         self.courses = courses if courses is not None else []
#
#     def enrol(self, course_name):
#         self.courses.append(course_name)
#
#     def drop(self, course_name):
#         if course_name in self.courses:
#             self.courses.remove(course_name)
#
#     def show_courses(self):
#         print(f"Enrolled in: {', '.join(self.courses)}")
#
# s = Student("Alice", "S001")
# print(f"Student: {s.name} (ID: {s.student_id})")
# s.enrol("Math")
# s.enrol("Science")
# s.enrol("English")
# s.show_courses()
# print("After dropping Science:")
# s.drop("Science")
# s.show_courses()


# # Question 2:
# class Time:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         if not (0 <= hours <= 23):
#             raise ValueError("Hours must be 0-23")
#         if not (0 <= minutes <= 59):
#             raise ValueError("Minutes must be 0-59")
#         if not (0 <= seconds <= 59):
#             raise ValueError("Seconds must be 0-59")
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#         self.period = "AM" if hours < 12 else "PM"
#
#     def total_seconds(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds
#
#     def display(self):
#         print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {self.period}")
#
# t1 = Time(14, 30, 45)
# t1.display()
# print(f"Total seconds: {t1.total_seconds()}")
# t2 = Time(9, 15)
# t2.display()
# print(f"Total seconds: {t2.total_seconds()}")


# # Question 3:
# class Product:
#     def __init__(self, name, price, stock=0):
#         self.name = name
#         self.price = price
#         self.stock = stock
#
#     def restock(self, quantity):
#         self.stock += quantity
#         print(f"Restocked {quantity} units. Stock: {self.stock}")
#
#     def sell(self, quantity):
#         if quantity <= self.stock:
#             self.stock -= quantity
#             print(f"Sold {quantity} units. Stock: {self.stock}")
#         else:
#             print(f"Cannot sell {quantity} units. Only {self.stock} in stock.")
#
#     def revenue(self, quantity):
#         return self.price * quantity
#
#     def info(self):
#         print(f"Product: {self.name} | Price: ${self.price} | Stock: {self.stock}")
#
# p = Product("Widget", 9.99)
# p.info()
# p.restock(100)
# p.sell(30)
# p.sell(80)
# print(f"Potential revenue for 50 units: ${p.revenue(50):.2f}")


# # Question 4:
# class Email:
#     def __init__(self, sender, recipient, subject="No Subject"):
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.body = ""
#         self.attachments = []
#
#     def write(self, text):
#         self.body = text
#
#     def attach(self, filename):
#         self.attachments.append(filename)
#
#     def preview(self):
#         print("===== EMAIL PREVIEW =====")
#         print(f"From: {self.sender}")
#         print(f"To: {self.recipient}")
#         print(f"Subject: {self.subject}")
#         if self.attachments:
#             print(f"Attachments: {', '.join(self.attachments)}")
#         print("---")
#         print(self.body)
#         print("=========================")
#
# email = Email("alice@mail.com", "bob@mail.com", "Meeting Tomorrow")
# email.write("Hi Bob, let's meet at 3pm to discuss the project.")
# email.attach("agenda.pdf")
# email.attach("notes.docx")
# email.preview()


# # Question 5:
# class QuizTracker:
#     def __init__(self, student_name, total_questions):
#         self.student_name = student_name
#         self.total_questions = total_questions
#         self.correct = 0
#         self.incorrect = 0
#         self.unanswered = total_questions
#
#     def answer(self, is_correct):
#         if self.unanswered > 0:
#             self.unanswered -= 1
#             if is_correct:
#                 self.correct += 1
#             else:
#                 self.incorrect += 1
#
#     def score_percentage(self):
#         return (self.correct / self.total_questions) * 100
#
#     def summary(self):
#         print(f"Quiz Summary for {self.student_name}")
#         print(f"Total Questions: {self.total_questions}")
#         print(f"Correct: {self.correct} | Incorrect: {self.incorrect} | Unanswered: {self.unanswered}")
#         print(f"Score: {self.score_percentage():.2f}%")
#         print(f"Result: {'PASS' if self.score_percentage() >= 50 else 'FAIL'}")
#
# q = QuizTracker("Charlie", 10)
# for answer in [True, True, False, True, True, True, True, False, True]:
#     q.answer(answer)
# q.summary()
