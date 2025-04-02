import argparse
import json
import os

TASK_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def main():
    """Main function to handle CLI commands."""
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add "add" command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)