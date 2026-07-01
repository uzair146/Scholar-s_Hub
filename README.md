# Scholar's Hub

A Student Management System with a built-in Quiz Game — built with Python and Tkinter.

## What is this project?

Scholar's Hub is a desktop application that helps manage student records and lets students test their knowledge through a random quiz. All data is saved locally so nothing is lost when you close the app.

## Features

- Add, search, and delete students
- Mark daily attendance
- Take a 5-question random quiz (50-question bank)
- View all students in a table
- Export full report to a text file
- Data saved automatically in JSON format

## Technologies Used

- Python 3
- Tkinter (GUI)
- JSON (file handling)
- OOP concepts (classes and objects)
- Exception handling

## How to Run

1. Make sure Python 3 is installed
2. Download the file `scholars_hub_gui.py`
3. Open terminal and run:python scholars_hub_gui.py

No extra libraries needed — all built-in!

## Concepts Covered

| Concept | How it's used |
|---|---|
| OOP | Student and DataManager classes |
| File Handling | JSON read/write for data storage |
| Exception Handling | Invalid inputs and missing files |
| GUI | Tkinter windows, buttons, forms |

## Project Structure

scholars_hub/
│
├── scholars_hub_gui.py   # Main application file
├── students.json         # Auto-created when you add students
└── report.txt            # Auto-created when you export report

## Author

**Muhammad Uzair Hussain**
