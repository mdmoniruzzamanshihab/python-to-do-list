# 📝 To-Do List (Core Python)

A lightweight command-line To-Do List application built using Core Python. This project helps users organize daily tasks by adding, viewing, and deleting tasks directly from the terminal. All tasks are automatically saved to a text file, ensuring they remain available even after the program is closed.

The project focuses on clean code, simplicity, and practical file handling without relying on external libraries or databases.

---

# Overview

This application demonstrates how a real-world task management system can be developed using only Python's built-in features. It is beginner-friendly while following a modular structure that makes the code easy to read, maintain, and extend.

---

# Features

- View all saved tasks
- Add new tasks
- Delete tasks by selecting their number
- Automatically save tasks after every change
- Load previously saved tasks on startup
- Gracefully handle invalid user input
- Lightweight and dependency-free
- Works directly from the terminal

---

# Why Use This Project?

Unlike a basic terminal To-Do List that loses all data after closing the program, this application provides persistent storage while keeping the implementation simple.

### Advantages

- Tasks are permanently stored in a text file.
- Existing tasks are loaded automatically when the application starts.
- No database installation or configuration is required.
- Uses only Python's standard library.
- Easy to understand and modify.
- Cross-platform compatibility.
- Suitable for Python beginners learning file handling.

---

# Performance & Efficiency

Although this is a beginner-level project, several design decisions improve its efficiency and maintainability.

- Tasks are loaded only once when the program starts.
- Data is written to the file only after adding or deleting a task.
- File operations are centralized in a reusable `save_tasks()` function.
- Uses a single list to manage all tasks efficiently.
- Minimal memory usage by storing only the task list.
- No third-party libraries, making the application lightweight and fast.

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Add Task | O(1) |
| Show Tasks | O(n) |
| Delete Task | O(n) |
| Load Tasks | O(n) |
| Save Tasks | O(n) |

---

# Technologies Used

- Python 3
- File Handling
- Lists
- Functions
- Loops
- Conditional Statements
- Exception Handling
- `os` Module

---

# Project Structure

```text
ToDo-List/
│
├── main.py
├── tasks.txt
└── README.md
```

---

# How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mdmoniruzzamanshihab/python-to-do-list
```

### 2. Navigate to the project folder

```bash
cd ToDo-List
```

### 3. Run the application

```bash
python main.py
```

---

# Application Menu

```text
WELCOME TO TO-DO LIST!

1. Show Tasks
2. Add Task
3. Delete Task
4. Exit
```

---

# Example

### Adding Tasks

```text
Enter new task:
Learn Python

Task added successfully!
```

### Viewing Tasks

```text
Your Tasks

1. Learn Python
2. Finish Assignment
3. Go to Gym
```

### Deleting a Task

```text
Enter task number to delete:

2

"Finish Assignment" deleted.
```

---

# Data Storage

Tasks are stored inside a plain text file named:

```text
tasks.txt
```

Example:

```text
Learn Python
Finish Assignment
Go to Gym
```

Whenever a task is added or deleted, the file is automatically updated.

---

# Error Handling

The application includes basic input validation.

- Prevents crashes when non-numeric values are entered.
- Detects invalid menu choices.
- Prevents deleting tasks from an empty list.
- Handles invalid task numbers safely.

---

# Concepts Practiced

- Variables
- Lists
- Functions
- While Loop
- For Loop
- Conditional Statements
- User Input
- File Handling
- Exception Handling (`try` / `except`)
- Built-in Functions (`len()`, `enumerate()`)
- File Context Manager (`with open`)
- `os.path.exists()`

---

# Future Improvements

- Edit existing tasks
- Mark tasks as completed
- Task priorities
- Due dates
- Categories
- Search functionality
- Sort tasks
- Colored terminal interface
- Export tasks
- Backup and restore tasks

---

# Why This Implementation?

This project emphasizes simplicity, readability, and practical programming concepts rather than unnecessary complexity.

Compared to many beginner implementations, it offers:

- Persistent data storage
- Automatic task loading
- Modular function design
- Input validation
- Reusable code
- Lightweight implementation
- Zero external dependencies
- Easy scalability for future features

---

# License

This project is open-source and available for learning, modification, and personal use.

---

Made with Core Python.