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
