"""
Simple CLI Task Manager

Features:
- Add tasks
- View tasks
- Delete tasks
- Quit the application
- Stores tasks in a Python list
"""

tasks = []

def display_menu():
    """Display the main menu options."""
    print("\n===== Task Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task():
    """Add a new task to the task list."""
    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("Invalid input. Task cannot be empty.")


def view_tasks():
    """Display all tasks in the task list."""
    if not tasks:
        print("There are no tasks to view.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def delete_task():
    """Delete a task from the task list."""
    try:
        if not tasks:
            print("There are no tasks to delete.")
            return

        view_tasks()
        task_number = int(input("Enter the number of the task to delete: "))

        if task_number < 1 or task_number > len(tasks):
            raise IndexError

    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("That task does not exist.")
    else:
        removed_task = tasks.pop(task_number - 1)
        print(f"Deleted task: {removed_task}")
    finally:
        print("Returning to main menu...")


def run_task_manager():
    """Run the main task manager application loop."""
    print("Welcome to the CLI Task Manager!")

    while True:
        display_menu()

        try:
            choice = int(input("Choose an option: "))

            if choice < 1 or choice > 4:
                raise ValueError

        except ValueError:
            print("Invalid menu option. Please choose 1, 2, 3, or 4.")
        else:
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Goodbye!")
                break
        finally:
            print("")


run_task_manager()