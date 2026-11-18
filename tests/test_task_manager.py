import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study Git")
        self.assertEqual(task["title"], "Study Git")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Finish lab")
        self.manager.complete_task(task["id"])
        self.assertTrue(self.manager.get_tasks()[0]["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Temp task")
        self.manager.delete_task(task["id"])
        self.assertEqual(self.manager.get_tasks(), [])

    def test_add_empty_task_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")


if __name__ == "__main__":
    unittest.main()