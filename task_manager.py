import json
from datetime import datetime


class Task:
    def __init__(self, id, title, description, category, due_date, priority, status="Не выполнена"):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }


class TaskManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description, category, due_date, priority):
        new_id = max((task.id for task in self.tasks), default=0) + 1
        new_task = Task(new_id, title, description, category, due_date, priority)
        self.tasks.append(new_task)
        self.save_tasks()

    def edit_task(self, task_id, **kwargs):
        task = self._find_task_by_id(task_id)
        if not task:
            raise ValueError(f"Задача с ID {task_id} не найдена.")
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        self.save_tasks()

    def delete_task(self, task_id):
        task = self._find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
        else:
            raise ValueError(f"Задача с ID {task_id} не найдена.")

    def search_tasks(self, keyword=None, category=None, status=None):
        result = self.tasks
        if keyword:
            result = [task for task in result if keyword.lower() in task.title.lower()]
        if category:
            result = [task for task in result if task.category.lower() == category.lower()]
        if status:
            result = [task for task in result if task.status.lower() == status.lower()]
        return result

    def mark_task_as_done(self, task_id):
        task = self._find_task_by_id(task_id)
        if task:
            task.status = "Выполнена"
            self.save_tasks()
        else:
            raise ValueError(f"Задача с ID {task_id} не найдена.")

    def save_tasks(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)

    def load_tasks(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                self.tasks = [Task.from_dict(task) for task in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def _find_task_by_id(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)
