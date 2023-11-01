class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def display_tasks(self):
        print("To-Do List:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}, Completed: {task.completed}")

        print("\nCompleted Tasks:")
        for index, task in enumerate(self.completed_tasks):
            print(f"{index + 1}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks.pop(task_index)
            task.completed = True
            self.completed_tasks.append(task)
        else:
            print("Invalid task index.")

    def update_task(self, task_index, description=None, due_date=None, priority=None):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            if description is not None:
                task.description = description
            if due_date is not None:
                task.due_date = due_date
            if priority is not None:
                task.priority = priority
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (or leave empty): ")
            priority = input("Enter priority (High/Medium/Low or leave empty): ")
            todo_list.add_task(description, due_date, priority)

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)

        elif choice == '4':
            task_index = int(input("Enter the task index to update: ") - 1)
            description = input("Enter new description (or leave empty): ")
            due_date = input("Enter new due date (or leave empty): ")
            priority = input("Enter new priority (High/Medium/Low or leave empty): ")
            todo_list.update_task(task_index, description, due_date, priority)

        elif choice == '5':
            task_index = int(input("Enter the task index to remove: ") - 1)
            todo_list.remove_task(task_index)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
