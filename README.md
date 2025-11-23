# Task-Project-List-CLI

A simple command-line task manager written in Python. It provides basic task operations (add, list, search, edit, remove, clear) and stores tasks in a JSON file (`tasks.json` by default).

FILES:
- task.py: main script that parses arguments and calls task functions.
- modifyTasks.py: module that defines add/list/search/edit/remove/clear operations on a JSON file.

PREREQUISITES:
- Python 3.8+ installed

EXAMPLES:

- Add a task (description with optional due date in YYYY-MM-DD):
    py .\task.py --add "Buy groceries" 2025-11-30

- List all tasks:
    py .\task.py --list

- Search tasks by keyword:
    py .\task.py --search groceries

- Edit a task (index, optional new description, optional new due date):
    py .\task.py --edit 0 "Buy groceries and snacks" 2025-12-01

- Remove a task by index:
    py .\task.py --remove 0

- Clear all tasks (will remove all entries from the file):
    py .\task.py --clear

- Use a custom tasks file:
py .\task.py --file mytasks.json --list