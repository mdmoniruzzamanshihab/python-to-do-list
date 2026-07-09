📝 To-Do List (Core Python)

A simple command-line To-Do List application built using Core Python. This project allows users to manage their daily tasks by adding, viewing, and deleting tasks. All tasks are automatically saved to a text file so they remain available even after the program is closed.
...... Features

*  View all tasks
*  Add new tasks
*  Delete existing tasks
*  Automatically save tasks to a text file
*  Load saved tasks when the program starts
*  Handles invalid user input gracefully

....... Technologies Used

* Python 3
* File Handling
* Lists
* Loops
* Functions
* Conditional Statements
* Exception Handling
* `os` Module

....... Project Structure

```text
ToDo-List/
│
├── main.py
├── tasks.txt
└── README.md
```

......How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```
.......Menu

```text
===== TO-DO LIST =====

1. Show Tasks
2. Add Task
3. Delete Task
4. Exit
```

.......Data Storage

Tasks are stored in a file named `tasks.txt`.

Example:

```text
Learn Python
Finish Assignment
Go to Gym
```

The application automatically loads existing tasks at startup and saves changes whenever a task is added or deleted.

.......Concepts Practiced

* Variables
* Lists
* Functions
* While Loop
* For Loop
* If / Elif / Else
* User Input
* File Handling
* Exception Handling (`try` / `except`)
* Built-in Functions (`len()`, `enumerate()`)
* `os.path.exists()`

....... Future Improvements

* Edit existing tasks
* Mark tasks as completed
* Add task priorities
* Search tasks
* Due dates
* Categories
* Colored terminal output


