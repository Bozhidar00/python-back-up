tasks = []


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")


def remove_task():
    if tasks:
        print("Current Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        index = int(input("Enter the number of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to remove.")


def view_tasks():
    if tasks:
        print("Current Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available.")


def main():
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
