class TaskManager:
    """Stores tasks in memory and provides add / list / complete / delete."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if title is None or not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = {"id": self.next_id, "title": title.strip(), "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        raise NotImplementedError("complete_task is not implemented yet")

    def delete_task(self, task_id):
        raise NotImplementedError("delete_task is not implemented yet")