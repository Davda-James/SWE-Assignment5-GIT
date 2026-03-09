import json


class ToDo:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []
        self.load_tasks()

    def add_task(self, task, priority):
        self.tasks.append({"task": task, "priority": priority})

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                return

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                self.completed_tasks.append(t)
                return

    def search_task(self, keyword):
        return [t for t in self.tasks if keyword.lower() in t["task"].lower()]

    def view_pending_tasks(self):
        return self.tasks

    def view_completed_tasks(self):
        return self.completed_tasks

    def stats(self):
        return {
            "pending": len(self.tasks),
            "completed": len(self.completed_tasks),
            "total": len(self.tasks) + len(self.completed_tasks),
        }

    def save_tasks(self):
        data = {"pending": self.tasks, "completed": self.completed_tasks}
        with open("tasks.json", "w") as f:
            json.dump(data, f)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                self.tasks = data["pending"]
                self.completed_tasks = data["completed"]
        except:
            pass


def main():
    todo = ToDo()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. View Pending Tasks")
        print("5. View Completed Tasks")
        print("6. Search Task")
        print("7. Show Statistics")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            priority = input("Priority (High/Medium/Low): ")
            todo.add_task(task, priority)
            print("Task added.")

        elif choice == "2":
            task = input("Task to remove: ")
            todo.remove_task(task)
            print("Task removed.")

        elif choice == "3":
            task = input("Task to complete: ")
            todo.complete_task(task)
            print("Task completed.")

        elif choice == "4":
            print("\nPending Tasks:")
            for i, t in enumerate(todo.view_pending_tasks(), 1):
                print(f"{i}. {t['task']} [{t['priority']}]")

        elif choice == "5":
            print("\nCompleted Tasks:")
            for i, t in enumerate(todo.view_completed_tasks(), 1):
                print(f"{i}. {t['task']} [{t['priority']}]")

        elif choice == "6":
            keyword = input("Search keyword: ")
            results = todo.search_task(keyword)
            print("\nSearch Results:")
            for t in results:
                print(f"- {t['task']} [{t['priority']}]")

        elif choice == "7":
            stats = todo.stats()
            print("\nStatistics")
            print("Total:", stats["total"])
            print("Pending:", stats["pending"])
            print("Completed:", stats["completed"])

        elif choice == "8":
            todo.save_tasks()
            print("Tasks saved. Exiting.")
            break

        else:
            print("Invalid choice.")


main()
