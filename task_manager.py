class TaskManager:
    """Stores tasks in memory and provides add / list / complete / delete."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = {"id": self.next_id, "title": title, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        raise NotImplementedError("complete_task is not implemented yet")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return task
        raise ValueError(f"No task found with ID {task_id}.")