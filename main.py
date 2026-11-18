from task_manager import TaskManager


def show_menu():
    print("\n=== Student Task Manager ===")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def display_tasks(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "[x]" if t["completed"] else "[ ]"
        print(f'{t["id"]}. {status} {t["title"]}')


def read_id():
    try:
        return int(input("Enter task ID: "))
    except ValueError:
        print("Error: ID must be a number.")
        return None


def main():
    manager = TaskManager()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        try:
            if choice == "1":
                task = manager.add_task(input("Task title: "))
                print(f'Added task {task["id"]}.')
            elif choice == "2":
                display_tasks(manager)
            elif choice == "3":
                task_id = read_id()
                if task_id is not None:
                    manager.complete_task(task_id)
                    print("Task marked as completed.")
            elif choice == "4":
                task_id = read_id()
                if task_id is not None:
                    manager.delete_task(task_id)
                    print("Task deleted.")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        except (ValueError, NotImplementedError) as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()