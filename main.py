class ToDO:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed_tasks.append(task)
        else:
            print("Task not found.")

    def clear_completed(self):
        self.completed_tasks.clear()

    def total_tasks(self):
        return len(self.tasks) + len(self.completed_tasks)

    def view_pending_tasks(self):
        return self.tasks

    def view_completed_tasks(self):
        return self.completed_tasks


def main():
    todo = ToDO()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. View Pending Tasks")
        print("5. View Completed Tasks")
        print("6. Show Total Tasks")
        print("7. Clear Completed Tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
            print(f"Task '{task}' added.")

        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo.remove_task(task)

        elif choice == "3":
            task = input("Enter the task to complete: ")
            todo.complete_task(task)

        elif choice == "4":
            pending_tasks = todo.view_pending_tasks()
            print("\nPending Tasks:")
            if not pending_tasks:
                print("No pending tasks.")
            for idx, task in enumerate(pending_tasks, 1):
                print(f"{idx}. {task}")

        elif choice == "5":
            completed_tasks = todo.view_completed_tasks()
            print("\nCompleted Tasks:")
            if not completed_tasks:
                print("No completed tasks.")
            for idx, task in enumerate(completed_tasks, 1):
                print(f"{idx}. {task}")

        elif choice == "6":
            print("Total tasks:", todo.total_tasks())

        elif choice == "7":
            todo.clear_completed()
            print("Completed tasks cleared.")

        elif choice == "8":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


main()
