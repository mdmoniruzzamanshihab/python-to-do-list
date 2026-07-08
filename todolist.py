import os

FILE_NAME = "tasks.txt"

tasks = []

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        tasks = [line.strip() for line in file]


def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


while True:
    print("\nWELCOME TO TO-DO LIST!")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks()
                    print(f'"{removed}" deleted.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")