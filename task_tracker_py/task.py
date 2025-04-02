from datetime import datetime
import json
import os

TASK_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

# create a Task class to represent a task
class Task:
    def __init__(self, id, description, status="todo",created_at=None, updated_at=None):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    # string representation of the task
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data): # create a task from a dictionary
        return cls(
            id=data["id"],
            description=data["description"],
            status=data["status"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

"""Load tasks to a JSON file."""
def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON. Starting with an empty task list.")
            return []

"""Save tasks to a JSON file."""
def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

"""Add a new task to the tasks.json file."""
def add_task(description):
    """Add a new task to the tasks.json file."""
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "Description": description,
        "Status": "todo",
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {new_task}")

"""List all tasks from the tasks.json file."""
def list_tasks():
    """List all tasks from the tasks.json file."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['Description']}, Status: {task['Status']}")
    print("Tasks loaded successfully.")

"""Update the status of a task."""
def update_task(task_id, status):
    """Update the status of a task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["Status"] = status
            save_tasks(tasks)
            print(f"Task {task_id} updated to {status}.")
            return
    print(f"Task {task_id} not found.")

"""Delete a task from the tasks.json file."""
def delete_task(task_id):
    """Delete a task from the tasks.json file."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")