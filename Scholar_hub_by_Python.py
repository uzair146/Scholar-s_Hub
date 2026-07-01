import json
import os
import random
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk
# Student class to store student data
class Student:
    def __init__(self, roll_no, name, class_name):
        self.roll_no = roll_no
        self.name = name
        self.class_name = class_name
        self.attendance = []
        self.quiz_scores = []
    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "class": self.class_name,
            "attendance": self.attendance,
            "quiz_scores": self.quiz_scores
        }
# Quiz questions database
QUESTIONS = [
    {"q": "What is the capital of Pakistan?", "options": ["Lahore", "Islamabad", "Karachi", "Multan"], "answer": "Islamabad"},
    {"q": "2 + 2 * 2 = ?", "options": ["6", "8", "4", "2"], "answer": "6"},
    {"q": "Who developed Python?", "options": ["Elon Musk", "Guido van Rossum", "Bill Gates", "Mark Zuckerberg"], "answer": "Guido van Rossum"},
    {"q": "Which is a Python data type?", "options": ["int", "varchar", "double", "char"], "answer": "int"},
    {"q": "HTML stands for?", "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "None"], "answer": "Hyper Text Markup Language"},
    {"q": "5 squared is?", "options": ["10", "25", "15", "20"], "answer": "25"},
    {"q": "Which one is a programming language?", "options": ["HTTP", "Python", "HTML", "CSS"], "answer": "Python"},
    {"q": "What does CPU stand for?", "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "None"], "answer": "Central Processing Unit"},
    {"q": "Pakistan got independence in?", "options": ["1945", "1947", "1950", "1971"], "answer": "1947"},
    {"q": "Which file stores Python code?", "options": [".py", ".exe", ".txt", ".java"], "answer": ".py"},
    {"q": "Which keyword is used to define a function in Python?", "options": ["function", "def", "func", "define"], "answer": "def"},
    {"q": "Which symbol is used for comments in Python?", "options": ["//", "#", "/*", "--"], "answer": "#"},
    {"q": "What is the output of 10 % 3?", "options": ["1", "3", "0", "10"], "answer": "1"},
    {"q": "Which data structure uses key-value pairs in Python?", "options": ["List", "Tuple", "Dictionary", "Set"], "answer": "Dictionary"},
    {"q": "Which loop is used when number of iterations is known?", "options": ["while", "for", "do-while", "if"], "answer": "for"},
    {"q": "What is the largest planet in our solar system?", "options": ["Earth", "Saturn", "Jupiter", "Mars"], "answer": "Jupiter"},
    {"q": "Who is known as the father of computers?", "options": ["Bill Gates", "Charles Babbage", "Steve Jobs", "Alan Turing"], "answer": "Charles Babbage"},
    {"q": "Which one is not a programming language?", "options": ["Java", "Python", "HTML", "C++"], "answer": "HTML"},
    {"q": "1 byte equals how many bits?", "options": ["4", "8", "16", "2"], "answer": "8"},
    {"q": "Which company developed Windows OS?", "options": ["Apple", "Microsoft", "Google", "IBM"], "answer": "Microsoft"},
    {"q": "Which sea is the saltiest in the world?", "options": ["Red Sea", "Dead Sea", "Black Sea", "Arabian Sea"], "answer": "Dead Sea"},
    {"q": "What does RAM stand for?", "options": ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Active Memory"], "answer": "Random Access Memory"},
    {"q": "Which country has the largest population?", "options": ["USA", "India", "China", "Russia"], "answer": "China"},
    {"q": "Which one is a mutable data type in Python?", "options": ["Tuple", "String", "List", "Integer"], "answer": "List"},
    {"q": "10 // 3 gives what result in Python?", "options": ["3.33", "3", "4", "1"], "answer": "3"},
    {"q": "Which keyword is used to handle exceptions in Python?", "options": ["catch", "except", "error", "handle"], "answer": "except"},
    {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": "Mars"},
    {"q": "Which is the longest river in the world?", "options": ["Amazon", "Nile", "Indus", "Ganges"], "answer": "Nile"},
    {"q": "What is the boiling point of water in Celsius?", "options": ["90", "100", "120", "80"], "answer": "100"},
    {"q": "Which gas do plants absorb from the air?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"q": "Who wrote the theory of relativity?", "options": ["Newton", "Einstein", "Darwin", "Tesla"], "answer": "Einstein"},
    {"q": "Which is the smallest prime number?", "options": ["0", "1", "2", "3"], "answer": "2"},
    {"q": "Which one is a NoSQL database?", "options": ["MySQL", "MongoDB", "PostgreSQL", "Oracle"], "answer": "MongoDB"},
    {"q": "Which operator is used for exponent in Python?", "options": ["^", "**", "%%", "//"], "answer": "**"},
    {"q": "Which one is a valid Python list?", "options": ["(1,2,3)", "[1,2,3]", "{1,2,3}", "<1,2,3>"], "answer": "[1,2,3]"},
    {"q": "Which continent is the Sahara Desert located in?", "options": ["Asia", "Africa", "Australia", "South America"], "answer": "Africa"},
    {"q": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "H2"], "answer": "H2O"},
    {"q": "Which year did World War 2 end?", "options": ["1942", "1945", "1939", "1950"], "answer": "1945"},
    {"q": "Which device is used to input sound into a computer?", "options": ["Speaker", "Microphone", "Monitor", "Printer"], "answer": "Microphone"},
    {"q": "Which one is an example of an operating system?", "options": ["Python", "Linux", "MySQL", "Excel"], "answer": "Linux"},
    {"q": "Which Pakistani city is known as the City of Lights?", "options": ["Lahore", "Karachi", "Islamabad", "Multan"], "answer": "Karachi"},
    {"q": "Which is the closest planet to the Sun?", "options": ["Venus", "Earth", "Mercury", "Mars"], "answer": "Mercury"},
    {"q": "Which loop runs at least once even if the condition is false?", "options": ["for", "while", "do-while", "nested loop"], "answer": "do-while"},
    {"q": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "Sequential Query Language"], "answer": "Structured Query Language"},
    {"q": "Which one is used to install Python packages?", "options": ["npm", "pip", "composer", "gem"], "answer": "pip"},
    {"q": "What is the value of True + True in Python?", "options": ["True", "2", "0", "Error"], "answer": "2"},
    {"q": "Which continent is the largest by area?", "options": ["Africa", "Asia", "Europe", "Antarctica"], "answer": "Asia"},
    {"q": "Which currency is used in Pakistan?", "options": ["Dollar", "Rupee", "Dinar", "Riyal"], "answer": "Rupee"},
    {"q": "Which keyword creates a class in Python?", "options": ["class", "object", "struct", "define"], "answer": "class"},
    {"q": "Which one is the fastest land animal?", "options": ["Lion", "Cheetah", "Horse", "Tiger"], "answer": "Cheetah"}
]
# Handles all file operations and data management
class DataManager:
    def __init__(self):
        self.students = []
        self.data_file = "students.json"
        self.load_data()
    # Load students from JSON file
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.students = []
                    for s in data:
                        student = Student(s["roll_no"], s["name"], s["class"])
                        student.attendance = s.get("attendance", [])
                        student.quiz_scores = s.get("quiz_scores", [])
                        self.students.append(student)
                print(f"Loaded {len(self.students)} students from file")
            except Exception as e:
                print(f"Error loading data: {e}")
                self.students = []
        else:
            print("No existing file found, starting fresh")
            self.students = []
    # Save students to JSON file
    def save_data(self):
        try:
            with open(self.data_file, "w") as f:
                data = [s.to_dict() for s in self.students]
                json.dump(data, f, indent=4)
            print(f"Saved {len(self.students)} students to file")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    # Find student by roll number
    def find_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                return s
        return None
    # Add new student
    def add_student(self, student):
        self.students.append(student)
        return self.save_data()
    # Delete student by roll number
    def delete_student(self, roll_no):
        student = self.find_student(roll_no)
        if student:
            self.students.remove(student)
            return self.save_data()
        return False
    # Update student attendance
    def update_student_attendance(self, roll_no, date):
        student = self.find_student(roll_no)
        if student:
            if date not in student.attendance:
                student.attendance.append(date)
                return self.save_data()
        return False
    # Update student quiz score
    def update_student_quiz(self, roll_no, score):
        student = self.find_student(roll_no)
        if student:
            student.quiz_scores.append(score)
            return self.save_data()
        return False
    # Export report to text file
    def export_report(self):
        if not self.students:
            return False
        try:
            with open("report.txt", "w") as f:
                f.write("=" * 50 + "\n")
                f.write("     SCHOLAR'S HUB - STUDENT REPORT\n")
                f.write("=" * 50 + "\n\n")
                for s in self.students:
                    f.write(f"Roll No: {s.roll_no}\n")
                    f.write(f"Name: {s.name}\n")
                    f.write(f"Class: {s.class_name}\n")
                    f.write(f"Attendance: {len(s.attendance)} days\n")
                    f.write(f"Quiz Scores: {s.quiz_scores}\n")
                    if s.quiz_scores:
                        avg = sum(s.quiz_scores) / len(s.quiz_scores)
                        f.write(f"Average Score: {avg:.1f}\n")
                    f.write("-" * 30 + "\n")
            return True
        except:
            return False
# Main application class
class ScholarsHubApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scholar's Hub - Student Management System")
        self.root.geometry("900x650")
        self.root.resizable(True, True)
        self.root.configure(bg='#2c3e50')
        self.data = DataManager()
        self.build_main_menu()
    # Clear all widgets from window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    # Build main menu screen
    def build_main_menu(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        title = tk.Label(self.root, text="Scholar's Hub", font=("Arial", 28, "bold"), bg='#2c3e50', fg='#e74c3c')
        title.pack(pady=15)
        subtitle = tk.Label(self.root, text="Student Management", font=("Arial", 14), bg='#2c3e50', fg='#f1c40f')
        subtitle.pack(pady=(0, 20))
        count_label = tk.Label(self.root, text=f"Total Students: {len(self.data.students)}", font=("Arial", 12), bg='#2c3e50', fg='#ecf0f1')
        count_label.pack(pady=(0, 15))
        buttons = [
            ("Add Student", '#27ae60'),
            ("Search Student", '#3498db'),
            ("Delete Student", '#e74c3c'),
            ("Show All Students", '#9b59b6'),
            ("Mark Attendance", '#f39c12'),
            ("Take Quiz", '#1abc9c'),
            ("Export Report", '#2ecc71'),
            ("Save & Exit", '#e74c3c')
        ]
        for text, color in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 11, "bold"), width=30, bg=color, fg='white', relief="raised", bd=3, cursor="hand2", command=lambda t=text: self.handle_button_click(t))
            btn.pack(pady=6)
    # Handle button clicks from main menu
    def handle_button_click(self, text):
        if "Add" in text:
            self.build_add_student()
        elif "Search" in text:
            self.build_search_student()
        elif "Delete" in text:
            self.build_delete_student()
        elif "Show" in text:
            self.build_show_all()
        elif "Attendance" in text:
            self.build_attendance()
        elif "Quiz" in text:
            self.build_quiz_start()
        elif "Export" in text:
            self.handle_export_report()
        elif "Exit" in text:
            self.handle_exit()
    # Add student screen
    def build_add_student(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        tk.Label(self.root, text="Add New Student", font=("Arial", 22, "bold"), bg='#2c3e50', fg='#e74c3c').pack(pady=20)
        tk.Label(self.root, text="Roll Number:", font=("Arial", 11), bg='#2c3e50', fg='#ecf0f1').pack(pady=(10,0))
        roll_entry = tk.Entry(self.root, width=35, font=("Arial", 11), bg='white', relief="solid", bd=2)
        roll_entry.pack(pady=5)
        tk.Label(self.root, text="Name:", font=("Arial", 11), bg='#2c3e50', fg='#ecf0f1').pack(pady=(10,0))
        name_entry = tk.Entry(self.root, width=35, font=("Arial", 11), bg='white', relief="solid", bd=2)
        name_entry.pack(pady=5)
        tk.Label(self.root, text="Class:", font=("Arial", 11), bg='#2c3e50', fg='#ecf0f1').pack(pady=(10,0))
        class_entry = tk.Entry(self.root, width=35, font=("Arial", 11), bg='white', relief="solid", bd=2)
        class_entry.pack(pady=5)
        def save_student():
            roll_no = roll_entry.get().strip()
            name = name_entry.get().strip()
            class_name = class_entry.get().strip()
            if not roll_no or not name or not class_name:
                messagebox.showerror("Error", "All fields are required!")
                return
            if self.data.find_student(roll_no):
                messagebox.showerror("Error", "Roll number already exists!")
                return
            new_student = Student(roll_no, name, class_name)
            if self.data.add_student(new_student):
                messagebox.showinfo("Success", f"Student '{name}' added successfully!")
                self.build_main_menu()
            else:
                messagebox.showerror("Error", "Failed to save student!")
        btn_frame = tk.Frame(self.root, bg='#2c3e50')
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Save Student", font=("Arial", 11, "bold"), width=20, bg='#27ae60', fg='white', command=save_student).pack(pady=5)
        tk.Button(btn_frame, text="Back to Menu", font=("Arial", 11, "bold"), width=20, bg='#3498db', fg='white', command=self.build_main_menu).pack(pady=5)
    # Search student screen
    def build_search_student(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        tk.Label(self.root, text="Search Student", font=("Arial", 22, "bold"), bg='#2c3e50', fg='#e74c3c').pack(pady=20)
        tk.Label(self.root, text="Enter Roll Number:", font=("Arial", 11), bg='#2c3e50', fg='#ecf0f1').pack(pady=(10,0))
        roll_entry = tk.Entry(self.root, width=35, font=("Arial", 11), bg='white', relief="solid", bd=2)
        roll_entry.pack(pady=5)
        result_frame = tk.Frame(self.root, bg='#2c3e50')
        result_frame.pack(pady=20)
        result_label = tk.Label(result_frame, text="", font=("Arial", 12), bg='#2c3e50', fg='#ecf0f1', justify="left")
        result_label.pack()
        def search():
            roll_no = roll_entry.get().strip()
            student = self.data.find_student(roll_no)
            if student:
                avg = "N/A"
                if student.quiz_scores:
                    avg = f"{sum(student.quiz_scores) / len(student.quiz_scores):.1f}"
                info = (f"Student Details:\n\nName: {student.name}\nClass: {student.class_name}\nAttendance: {len(student.attendance)} days\nQuiz Scores: {student.quiz_scores}\nAverage Score: {avg}")
                result_label.config(text=info, fg='#2ecc71')
            else:
                result_label.config(text="Student not found!", fg='#e74c3c')
        btn_frame = tk.Frame(self.root, bg='#2c3e50')
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Search", font=("Arial", 11, "bold"), width=20, bg='#3498db', fg='white', command=search).pack(pady=5)
        tk.Button(btn_frame, text="Back to Menu", font=("Arial", 11, "bold"), width=20, bg='#f39c12', fg='white', command=self.build_main_menu).pack(pady=5)
    # Delete student screen
    def build_delete_student(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        tk.Label(self.root, text="Delete Student", font=("Arial", 22, "bold"), bg='#2c3e50', fg='#e74c3c').pack(pady=20)
        tk.Label(self.root, text="Warning: This action cannot be undone!", font=("Arial", 12), bg='#2c3e50', fg='#f39c12').pack(pady=5)
        tk.Label(self.root, text="Enter Roll Number:", font=("Arial", 11), bg='#2c3e50', fg='#ecf0f1').pack(pady=(10,0))
        roll_entry = tk.Entry(self.root, width=35, font=("Arial", 11), bg='white', relief="solid", bd=2)
        roll_entry.pack(pady=5)
        def delete():
            roll_no = roll_entry.get().strip()
            student = self.data.find_student(roll_no)
            if student:
                if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{student.name}'?"):
                    if self.data.delete_student(roll_no):
                        messagebox.showinfo("Success", "Student deleted successfully!")
                        self.build_main_menu()
                    else:
                        messagebox.showerror("Error", "Failed to delete student!")
            else:
                messagebox.showerror("Error", "Student not found!")
        btn_frame = tk.Frame(self.root, bg='#2c3e50')
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Delete", font=("Arial", 11, "bold"), width=20, bg='#e74c3c', fg='white', command=delete).pack(pady=5)
        tk.Button(btn_frame, text="Back to Menu", font=("Arial", 11, "bold"), width=20, bg='#3498db', fg='white', command=self.build_main_menu).pack(pady=5)
    # Show all students screen
    def build_show_all(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        tk.Label(self.root, text="All Students", font=("Arial", 22, "bold"), bg='#2c3e50', fg='#e74c3c').pack(pady=20)
        if not self.data.students:
            tk.Label(self.root, text="No students added yet!", font=("Arial", 14), bg='#2c3e50', fg='#f39c12').pack(pady=40)
        else:
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview", background="white", foreground="black", rowheight=25, font=("Arial", 10))
            style.configure("Treeview.Heading", background="#3498db", foreground="white", font=("Arial", 11, "bold"))
            frame = tk.Frame(self.root, bg='#2c3e50')
            frame.pack(pady=10)
            columns = ("Roll No", "Name", "Class")
            tree = ttk.Treeview(frame, columns=columns, show="headings", height=12)
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=200, anchor="center")
            tree.pack()
            for s in self.data.students:
                tree.insert("", "end", values=(s.roll_no, s.name, s.class_name))
        tk.Button(self.root, text="Back to Menu", font=("Arial", 11, "bold"), width=20, bg='#3498db', fg='white', command=self.build_main_menu).pack(pady=20)
    # Mark attendance screen
    def build_attendance(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        tk.Label(self.root, text="Mark Attendance", font=("Arial", 22, "bold"), bg='#2c3e50', fg='#e74c3c').pack(pady=20)
        tk.Label(self.root, text="Enter Roll Number:", font=("Arial", 11), bg='#2c3e50', fg='#ecf0f1').pack(pady=(10,0))
        roll_entry = tk.Entry(self.root, width=35, font=("Arial", 11), bg='white', relief="solid", bd=2)
        roll_entry.pack(pady=5)
        def mark():
            roll_no = roll_entry.get().strip()
            student = self.data.find_student(roll_no)
            if student:
                today = datetime.now().strftime("%Y-%m-%d")
                if today in student.attendance:
                    messagebox.showinfo("Info", "Attendance already marked for today!")
                else:
                    if self.data.update_student_attendance(roll_no, today):
                        messagebox.showinfo("Success", f"Attendance marked for {student.name}!")
                        self.build_main_menu()
                    else:
                        messagebox.showerror("Error", "Failed to mark attendance!")
            else:
                messagebox.showerror("Error", "Student not found!")
        btn_frame = tk.Frame(self.root, bg='#2c3e50')
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Mark Present", font=("Arial", 11, "bold"), width=20, bg='#27ae60', fg='white', command=mark).pack(pady=5)
        tk.Button(btn_frame, text="Back to Menu", font=("Arial", 11, "bold"), width=20, bg='#3498db', fg='white', command=self.build_main_menu).pack(pady=5)
    # Start quiz screen
    def build_quiz_start(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        tk.Label(self.root, text="Take Quiz", font=("Arial", 22, "bold"), bg='#2c3e50', fg='#e74c3c').pack(pady=20)
        tk.Label(self.root, text="5 Random Questions - Test Your Knowledge!", font=("Arial", 12), bg='#2c3e50', fg='#f1c40f').pack(pady=5)
        tk.Label(self.root, text="Enter Your Roll Number:", font=("Arial", 11), bg='#2c3e50', fg='#ecf0f1').pack(pady=(10,0))
        roll_entry = tk.Entry(self.root, width=35, font=("Arial", 11), bg='white', relief="solid", bd=2)
        roll_entry.pack(pady=5)
        def start():
            roll_no = roll_entry.get().strip()
            student = self.data.find_student(roll_no)
            if student:
                self.current_quiz_student = student
                self.quiz_questions = random.sample(QUESTIONS, 5)
                self.quiz_index = 0
                self.quiz_score = 0
                self.build_quiz_question()
            else:
                messagebox.showerror("Error", "Student not found! Please add yourself first.")
        btn_frame = tk.Frame(self.root, bg='#2c3e50')
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Start Quiz", font=("Arial", 11, "bold"), width=20, bg='#27ae60', fg='white', command=start).pack(pady=5)
        tk.Button(btn_frame, text="Back to Menu", font=("Arial", 11, "bold"), width=20, bg='#3498db', fg='white', command=self.build_main_menu).pack(pady=5)
    # Quiz question screen
    def build_quiz_question(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        question = self.quiz_questions[self.quiz_index]
        tk.Label(self.root, text=f"Question {self.quiz_index + 1} of 5", font=("Arial", 16, "bold"), bg='#2c3e50', fg='#f1c40f').pack(pady=10)
        tk.Label(self.root, text=question["q"], font=("Arial", 14), wraplength=600, justify="center", bg='#2c3e50', fg='#ecf0f1').pack(pady=20)
        self.selected_option = tk.StringVar()
        for option in question["options"]:
            rb = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=option, font=("Arial", 12), bg='#2c3e50', fg='#ecf0f1', selectcolor='#3498db', cursor="hand2")
            rb.pack(anchor="w", padx=150, pady=5)
        def submit_answer():
            chosen = self.selected_option.get()
            if not chosen:
                messagebox.showwarning("Warning", "Please select an option!")
                return
            if chosen == question["answer"]:
                self.quiz_score += 1
            self.quiz_index += 1
            if self.quiz_index < len(self.quiz_questions):
                self.build_quiz_question()
            else:
                self.build_quiz_result()
        tk.Button(self.root, text="Next", font=("Arial", 11, "bold"), width=20, bg='#3498db', fg='white', command=submit_answer).pack(pady=20)
    # Quiz result screen
    def build_quiz_result(self):
        self.clear_window()
        self.root.configure(bg='#2c3e50')
        self.data.update_student_quiz(self.current_quiz_student.roll_no, self.quiz_score)
        tk.Label(self.root, text="Quiz Completed!", font=("Arial", 26, "bold"), bg='#2c3e50', fg='#e74c3c').pack(pady=40)
        score_color = '#2ecc71' if self.quiz_score >= 4 else '#f39c12' if self.quiz_score >= 3 else '#e74c3c'
        tk.Label(self.root, text=f"Score: {self.quiz_score} / 5", font=("Arial", 22, "bold"), bg='#2c3e50', fg=score_color).pack(pady=20)
        if self.quiz_score == 5:
            msg = "Perfect! You're a genius!"
        elif self.quiz_score >= 4:
            msg = "Excellent performance!"
        elif self.quiz_score >= 3:
            msg = "Good effort! Keep practicing!"
        else:
            msg = "Keep learning! Practice makes perfect!"
        tk.Label(self.root, text=msg, font=("Arial", 14), bg='#2c3e50', fg='#f1c40f').pack(pady=10)
        tk.Button(self.root, text="Back to Menu", font=("Arial", 11, "bold"), width=20, bg='#3498db', fg='white', command=self.build_main_menu).pack(pady=30)
    # Export report handler
    def handle_export_report(self):
        if not self.data.students:
            messagebox.showinfo("Info", "No students to export!")
            return
        if self.data.export_report():
            messagebox.showinfo("Success", "Report exported as 'report.txt'")
        else:
            messagebox.showerror("Error", "Failed to export report!")
    # Save and exit handler
    def handle_exit(self):
        if self.data.save_data():
            messagebox.showinfo("Success", "Data saved successfully!\nGoodbye!")
        else:
            messagebox.showerror("Error", "Failed to save data!")
        self.root.destroy()
# Run the application
def main():
    root = tk.Tk()
    app = ScholarsHubApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
