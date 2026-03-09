import json


class ToDo:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []
        self.load_tasks()

    def add_task(self, task, priority, due_date):
        self.tasks.append({"task": task, "priority": priority, "due_date": due_date})

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.completed_tasks.append(task)
        else:
            print("Task not found.")

    def clear_completed(self):
        self.completed_tasks.clear()

    def total_tasks(self):
        return len(self.tasks) + len(self.completed_tasks)

    def edit_task(self, index, new_task, new_priority, new_due):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            self.tasks[index]["priority"] = new_priority
            self.tasks[index]["due_date"] = new_due

    def search_task(self, keyword):
        return [t for t in self.tasks if keyword.lower() in t["task"].lower()]

    def sort_by_priority(self):
        order = {"High": 1, "Medium": 2, "Low": 3}
        self.tasks.sort(key=lambda x: order.get(x["priority"], 4))

    def clear_completed(self):
        self.completed_tasks = []

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


def show_tasks(tasks):
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['task']} | Priority: {t['priority']} | Due: {t['due_date']}")


def main():
    todo = ToDo()

    while True:
        print("\n====== TO DO APP ======")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. View Pending Tasks")
        print("5. View Completed Tasks")
        print("6. Search Task")
        print("7. Show Statistics")
        print("8. Edit Task")
        print("9. Sort by Priority")
        print("10. Clear Completed Tasks")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Task: ")
            priority = input("Priority (High/Medium/Low): ")
            due = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(task, priority, due)
            print("Task added.")

        elif choice == "2":
            show_tasks(todo.tasks)
            index = int(input("Task number to remove: ")) - 1
            todo.remove_task(index)

        elif choice == "3":
            show_tasks(todo.tasks)
            index = int(input("Task number to complete: ")) - 1
            todo.complete_task(index)

        elif choice == "4":
            print("\nPending Tasks:")
            show_tasks(todo.tasks)

        elif choice == "5":
            print("\nCompleted Tasks:")
            show_tasks(todo.completed_tasks)

        elif choice == "6":
            keyword = input("Search keyword: ")
            results = todo.search_task(keyword)
            show_tasks(results)

        elif choice == "7":
            stats = todo.stats()
            print("\nStatistics")
            print("Total:", stats["total"])
            print("Pending:", stats["pending"])
            print("Completed:", stats["completed"])

        elif choice == "8":
            show_tasks(todo.tasks)
            index = int(input("Task number to edit: ")) - 1
            new_task = input("New task: ")
            new_priority = input("New priority: ")
            new_due = input("New due date: ")
            todo.edit_task(index, new_task, new_priority, new_due)

        elif choice == "9":
            todo.sort_by_priority()
            print("Tasks sorted by priority.")

        elif choice == "10":
            todo.clear_completed()
            print("Completed tasks cleared.")

        elif choice == "11":
            todo.save_tasks()
            print("Tasks saved. Exiting.")
            break

        else:
            print("Invalid choice.")


main()
