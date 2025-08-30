# todo.py

import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from file into a list."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]


def save_tasks(tasks):
    """Save tasks back to file."""
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def list_tasks(tasks):
    """Print all tasks with numbers."""
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    """Add a new task from user input."""
    description = input("Enter task description: ").strip()
    if description:
        tasks.append(description)
        save_tasks(tasks)
        print("Task added!")


def delete_task(tasks):
    """Delete a task by its number."""
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()