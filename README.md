# 📝 Command-Line To-Do Manager (Python)

A simple CLI-based To-Do list manager built in **Python 3** using only the standard library.
This project is designed for beginners to practice **data structures**, **file I/O**, and **CLI handling**.

---

## 🚀 Features
- Add new tasks
- View all tasks
- Delete tasks by number
- Persistent storage (`tasks.txt`)
- User-friendly CLI with `argparse`

---

## 📂 Project Structure
.
├── todo.py      # Main script
└── tasks.txt    # Tasks storage (auto-created)


---

## ⚡ Installation
Clone the repo and run with Python 3:

```bash
git clone [https://github.com/your-username/todo-cli.git](https://github.com/your-username/todo-cli.git)
cd todo-cli
No external dependencies are required.

🛠️ Usage
Add a Task
Bash

python todo.py add "Buy groceries"
View Tasks
Bash

python todo.py view
Delete a Task
Bash

python todo.py delete 2
📌 Example
Bash

$ python todo.py add "Finish Python project"
✅ Task added: Finish Python project

$ python todo.py add "Read a book"
✅ Task added: Read a book

$ python todo.py view
📋 Your To-Do List:
1. Finish Python project
2. Read a book

$ python todo.py delete 1
🗑️ Task deleted: Finish Python project
🧰 Tools & Technologies
Python 3

Standard Library (argparse, os)

🤝 Contributing
Fork, add features (like update tasks, mark as done, deadlines), and create a PR 🚀.

📜 License
MIT License

