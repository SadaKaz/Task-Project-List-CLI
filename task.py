#main function for task management CLI
from modifyTasks import add_task, list_tasks, search_tasks, edit_task, remove_task, clear_tasks
import argparse

# parse CLI arguments
parser = argparse.ArgumentParser(description="Task Management CLI")
# add arguments
parser.add_argument('--add', nargs='+', help='Add a new task with optional due date. Usage: --add "task description" [due date YYYY-MM-DD]', metavar=('TASK'))
parser.add_argument('--list', action='store_true', help='List all tasks')
parser.add_argument('--search', type=str, help='Search tasks by keyword', metavar='KEYWORD')
parser.add_argument('--edit', nargs='+', help='Edit an existing task. Usage: --edit task_index ["new description"] [new_due_date]', metavar=('INDEX'))
parser.add_argument('--file', type=str, default='tasks.json', help='Specify the tasks file (default: tasks.json)', metavar='FILE')
parser.add_argument('--remove', type=int, help='Remove a task by its index', metavar='INDEX')
parser.add_argument('--clear', action='store_true', help='Clear all tasks from the file')
# parse arguments
args = parser.parse_args()

# execute based on arguments
if args.add:
    task_description = args.add[0]
    if len(args.add) > 1:
        due_date = args.add[1]
    else:
        due_date = None
    add_task(args.file, task_description, due_date)
elif args.list:
    list_tasks(args.file)
elif args.search:
    search_tasks(args.file, args.search)
elif args.edit:
    try:
        task_index = int(args.edit[0])
        new_description = args.edit[1] if len(args.edit) > 1 else None
        new_due_date = args.edit[2] if len(args.edit) > 2 else None
        edit_task(args.file, task_index, new_description, new_due_date)
    except ValueError:
        print("Error: Task index must be an integer.")
elif args.remove:
    remove_task(args.file, args.remove)
elif args.clear:
    clear_tasks(args.file)
else:
    parser.print_help()
