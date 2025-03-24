🛠️ User Registry System (Updated)
This is an open-source Python project built with PyQt5, designed for user data management.
It allows users to input personal details, generate unique identification codes, store and retrieve user data, and manage records efficiently.

🔹 License: Apache License 2.0
🔹 Author: AlexNT-maker

✨ Features
✔️ User-friendly GUI – Built with PyQt5
✔️ Unique user code generation 🔢
✔️ Store user data (name, surname, city, phone) in save.txt 📄
✔️ Retrieve users by their unique code 🔍
✔️ Automatic list clearing after saving to avoid duplicates
✔️ Separate storage for unique codes in code_set.txt 🔑
✔️ Data persistence across sessions 💾



📂 Project Structure
bash
Copy
Edit
UserRegistry/
│
├── main_program.py      # Main GUI application
├── file_handler.py      # Handles user data storage, retrieval, and unique code generation
├── Person.py            # Defines the Person class for user management
├── save.txt             # Auto-created file storing user data
├── code_set.txt         # Auto-created file storing unique user codes
├── README.md            # Project documentation
├── requirements.txt     # Dependencies required for the project
└── .gitignore           # Excludes unnecessary files (to be added)

⚙️ Installation & Setup
Prerequisites
Python 3.x installed on your system

Recommended IDE: Spyder (Anaconda), VS Code, or PyCharm

