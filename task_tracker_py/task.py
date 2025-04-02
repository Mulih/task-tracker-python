from datetime import datetime

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