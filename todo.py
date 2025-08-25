#!/usr/bin/env python3
"""
Command-Line To-Do Manager
--------------------------
A simple CLI-based to-do list app.

Features:
- Add tasks
- View tasks
- Delete tasks (by index)
- Persistent storage in tasks.txt

Usage:
    python todo.py add "Buy groceries"
    python todo.py view
    python todo.py delete 2
"""

import argparse
import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the file, return as a list."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def save_tasks(tasks):
    """Save the list of tasks back to file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks found. Your to-do list is empty.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed}")
    else:
        print(f"❌ Invalid task number: {index}")


def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI To-Do List Manager"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="Task description")

    # View command
    subparsers.add_parser("view", help="View all tasks")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Task number to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "view":
        view_tasks()
    elif args.command == "delete":
        delete_task(args.index)


if __name__ == "__main__":
    main()
