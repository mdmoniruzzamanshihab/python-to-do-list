# To-Do List | Core Python

A lightweight command-line To-Do List application developed using Core Python. It allows users to manage daily tasks by adding, viewing, and deleting tasks directly from the terminal.

The application features automatic file-based data persistence, ensuring that saved tasks remain available even after the program is closed.

Built with simplicity, clean code, and modular design in mind, without external libraries or database dependencies.

---

## Overview

This project demonstrates how to build a simple task management application using Python's built-in features. It follows a modular structure that promotes readability, maintainability, and future scalability.

## Features

- View all saved tasks
- Add new tasks
- Delete tasks by selecting their numbers
- Automatically save changes to a text file
- Load existing tasks on startup
- Validate user input and handle invalid entries
- Prevent deletion from an empty task list
- Lightweight and dependency-free
- Cross-platform terminal support

## Why Use This Project?

Unlike basic command-line applications that lose data after closing, this application provides persistent storage while maintaining a simple implementation.

**Key Advantages**

- Permanent task storage using a text file.
- Automatic task loading on startup.
- No database installation or configuration.
- Uses only Python's standard library.
- Beginner-friendly and easy to extend.
- Minimal resource consumption.

---

## Performance & Efficiency

The application uses a simple and efficient approach to task management.

- Tasks are loaded once during startup.
- File updates occur only when tasks are added or deleted.
- File operations are centralized in a reusable `save_tasks()` function.
- A single list manages all tasks.
- Minimal memory overhead.
- No third-party dependencies.

### Time Complexity

Let `n` represent the total number of stored tasks.

| Operation | Time Complexity |
|---|---|
| Add Task (List) | O(1) |
| Show Tasks | O(n) |
| Delete Task | O(n) |
| Load Tasks | O(n) |
| Save Tasks | O(n) |

*Note: The complete Add Task operation, including rewriting the file, takes O(n) time.*

---

## Technologies Used

- Python 3
- File Handling
- Lists and Functions
- Loops and Conditional Statements
- Exception Handling
- `os` Module

---

## Project Structure

```text
ToDo-List/
│
├── main.py
├── tasks.txt
└── README.md
```

---

## How to Run

**1. Clone the Repository**

```bash
git clone https://github.com/mdmoniruzzamanshihab/python-to-do-list.git
```

**2. Navigate to the Project Directory**

```bash
cd ToDo-List
```

**3. Run the Application**

```bash
python main.py
```

---

## Application Menu

```text
WELCOME TO TO-DO LIST!

1. Show Tasks
2. Add Task
3. Delete Task
4. Exit
```

---

## Example Usage

**Adding Tasks**

```text
Enter new task:
Learn Python

Task added successfully!
```

**Viewing Tasks**

```text
Your Tasks

1. Learn Python
2. Finish Assignment
3. Go to Gym
```

**Deleting a Task**

```text
Enter task number to delete:

2

"Finish Assignment" deleted.
```

---

## Data Storage

All tasks are stored in a local text file named `tasks.txt`.

**Example:**

```text
Learn Python
Finish Assignment
Go to Gym
```

The application automatically loads existing tasks when launched and updates the file whenever a task is added or deleted.

---

## Error Handling

The application includes basic input validation to ensure reliable operation.

- Handles non-numeric input safely.
- Detects invalid menu selections.
- Prevents deletion from an empty list.
- Validates selected task numbers.
- Handles missing task files during startup.

---

## Concepts Practiced

- Variables and Data Types
- Lists
- Functions
- While and For Loops
- Conditional Statements
- User Input
- File Handling
- Exception Handling (`try` / `except`)
- Built-in Functions (`len()`, `enumerate()`)
- File Context Manager (`with open()`)
- File System Operations (`os.path.exists()`)

---

## Future Improvements

- Edit existing tasks
- Mark tasks as completed
- Task priorities
- Due dates and categories
- Search and sorting functionality
- Colored terminal interface
- Export task data
- Backup and restore functionality

---

## License

This project is open-source and available for learning, modification, and personal use.

---

**Made with Core Python.**