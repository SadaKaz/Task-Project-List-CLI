# modules for modifying tasks
import json
import os
from datetime import datetime

# load/create JSON file
def load (filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Error: Corrupted file. Starting with an empty task list.")
            return []
        
# save tasks to JSON file
def save (filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# add a new task
def add_task (filename, task_description, due_date=None):
    tasks = load(filename)
    timestamp = datetime.now().isoformat()
    task = {
        "description": task_description,
        "timestamp": timestamp,
        "due_date": due_date
    }
    tasks.append(task)
    save(filename, tasks)
    print("Task added successfully.")

# list all tasks
def list_tasks (filename):
    tasks = load(filename)
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        due = task["due_date"] if task["due_date"] else "No due date"
        print(f"{idx}. {task['description']} (Added: {task['timestamp']}, Due: {due})")

# search tasks by keyword
def search_tasks (filename, keyword):
    tasks = load(filename)
    found_tasks = [task for task in tasks if keyword.lower() in task["description"].lower()]
    if not found_tasks:
        print("No matching tasks found.")
        return
    for idx, task in enumerate(found_tasks, start=1):
        due = task["due_date"] if task["due_date"] else "No due date"
        print(f"{idx}. {task['description']} (Added: {task['timestamp']}, Due: {due})")

# edit an existing task
def edit_task (filename, task_index, new_description=None, new_due_date=None):
    tasks = load(filename)
    if task_index < 1 or task_index > len(tasks):
        print("Error: Task index out of range.")
        return
    if new_description:
        tasks[task_index - 1]["description"] = new_description
    if new_due_date is not None:
        tasks[task_index - 1]["due_date"] = new_due_date
    save(filename, tasks)
    print("Task updated successfully.")