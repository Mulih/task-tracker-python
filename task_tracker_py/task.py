from datetime import datetime
import json
import os

TASK_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

class Task:
    def __init__(self, id, description, status="todo",created_at=None, updated_at=None):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()


    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            description=data["description"],
            status=data["status"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )


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

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
