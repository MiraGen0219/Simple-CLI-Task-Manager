# CLI Task Manager

A simple Command Line Interface (CLI) Task Manager application built with Python.

This project allows users to:
- Add tasks
- View tasks
- Delete tasks
- Quit the application

The application stores tasks using a Python list and demonstrates foundational Python programming concepts such as:
- Functions
- Lists
- Loops
- Conditionals
- Error Handling
- User Input
- Docstrings

---

# Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How to Use](#how-to-use)
- [Error Handling](#error-handling)
- [Concepts Practiced](#concepts-practiced)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

# Features

- Add tasks to a task list
- View all current tasks
- Delete tasks by selecting task number
- Input validation for invalid menu choices
- Error handling using:
  - `try`
  - `except`
  - `else`
  - `finally`
- Clean and organized function-based structure
- Descriptive docstrings and comments

---

# Technologies Used

- Python 3

---

# Project Structure

```text
task-manager/
│
├── task_manager.py
└── README.md

---

# Lessons Learned During Development

## 🖥️ Using `\n` for Cleaner Terminal Output

One important concept learned during development was the use of the newline character:

```python
print("\n===== Task Manager =====")
```

The `\n` character creates spacing in the terminal output, making the application's interface cleaner and easier to read.

Without spacing, terminal applications can quickly become cluttered and difficult for users to follow. This project demonstrated how even small formatting improvements can significantly improve the user experience in a Command Line Interface (CLI) application.

### Example

Without `\n`:

```text
Task added: Homework
===== Task Manager =====
```

With `\n`:

```text
Task added: Homework

===== Task Manager =====
```

The additional spacing creates a cleaner and more organized interface.

---

## ⚠️ Designing an Application with Multiple Error Catch Features

Another major lesson learned during development was the importance of error handling and defensive programming.

This application was intentionally designed with several layers of input validation and error-catching features to prevent the program from crashing when users provide invalid or unexpected input.

### Error Handling Features Included

✅ Prevent invalid menu selections

✅ Catch non-numeric input using `try` and `except`

✅ Prevent deletion of tasks that do not exist

✅ Alert users when there are no tasks to view

✅ Alert users when there are no tasks to delete

✅ Prevent empty task submissions

---

## 🧠 Example of Error Handling

```python
try:
    task_number = int(input("Enter the number of the task to delete: "))

    if task_number < 1 or task_number > len(tasks):
        raise IndexError

except ValueError:
    print("Invalid input. Please enter a number.")

except IndexError:
    print("That task does not exist.")
```

This section of code helped reinforce understanding of:

- `try`
- `except`
- `else`
- `finally`
- input validation
- defensive programming
- user experience design

---

## 🚀 Overall Development Takeaways

Through this project, important foundational programming skills were strengthened, including:

- Writing organized functions
- Structuring a CLI application
- Handling user input safely
- Designing user-friendly terminal output
- Creating maintainable Python code
- Building applications that can gracefully recover from user mistakes

This project demonstrated that even a simple CLI application benefits greatly from thoughtful formatting, structure, and robust error handling.
