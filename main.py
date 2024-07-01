import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pandas as pd

names = [
  { "name" : "Abhishek Paul", "rollNo" : 22015301, "imgSrc" : "https://i.pinimg.com/564x/71/f9/95/71f99570b5de56dfec7d3290389c1d4f.jpg" },
  { "name" : "ADITYA KUMAR SINGH", "rollNo" : 22015302, "imgSrc" : "https://i.pinimg.com/564x/c2/4d/fb/c24dfbb0dad1a14d27c7a0a365c6ba3e.jpg" },
  { "name" : "Akash Sharma", "rollNo" : 22015303, "imgSrc" : "https://i.pinimg.com/564x/0c/44/f3/0c44f30df3d1ac40372ae95e45d87036.jpg" },
  { "name" : "ANJALI", "rollNo" : 22015304, "imgSrc" : "https://i.pinimg.com/564x/49/37/98/49379839eb02d32bed28e0ff00c03627.jpg" },
  { "name" : "ANSH TRIPATHI", "rollNo" : 22015305, "imgSrc" : "https://i.pinimg.com/564x/ae/3e/d5/ae3ed59ff42ff806fafe30d48bf126fd.jpg" },
  { "name" : "Arvind Soni", "rollNo" : 22015307, "imgSrc" : "https://i.pinimg.com/736x/04/5b/47/045b475d0fc61904e690e7ee5f566777.jpg" },
  { "name" : "Ayush rai", "rollNo" : 22015308, "imgSrc" : "https://i.pinimg.com/564x/dd/7e/8d/dd7e8d5ad81a6e18e108ac9f1f6ce277.jpg" },
  { "name" : "B Vamsi", "rollNo" : 22015309, "imgSrc" : "https://i.pinimg.com/564x/72/d8/38/72d838bdfdd38b94c784cb3d9c26f2ca.jpg" },
  { "name" : "Bipasha Mallick", "rollNo" : 22015310, "imgSrc" : "https://i.pinimg.com/564x/96/00/88/960088df941dc2bf5f9b444c51fe9f3f.jpg" },
  { "name" : "CHITESH KUMAR SAHU", "rollNo" : 22015311, "imgSrc" : "https://i.pinimg.com/564x/07/43/b5/0743b568782715caf5dd4e782e0fee60.jpg" },
  { "name" : "HARSHVARDHAN KUMAR", "rollNo" : 22015312, "imgSrc" : "https://i.pinimg.com/564x/f6/40/8d/f6408d8419bed11cd42d7ae941245d4c.jpg" },
  { "name" : "HEENA KUMARI SAHU", "rollNo" : 22015313, "imgSrc" : "https://i.pinimg.com/564x/00/c8/73/00c873e7b60fdefc66c9b2d76570c388.jpg" },
  { "name" : "HITESH KHUNTE", "rollNo" : 22015314, "imgSrc" : "https://i.pinimg.com/564x/12/de/75/12de7558a6c275ef94c48cb2fae8fa6d.jpg" },
  { "name" : "HRISHABH YADAV", "rollNo" : 22015315, "imgSrc" : "https://i.pinimg.com/564x/e4/da/39/e4da393d452dc282973deedf71092413.jpg" },
  { "name" : "Krishna Pandey", "rollNo" : 22015316, "imgSrc" : "https://i.pinimg.com/564x/36/b6/8a/36b68a8bda77a30f6290b7bb98c6b3d8.jpg" },
  { "name" : "KUMAR SHUBHRANSHU", "rollNo" : 22015317, "imgSrc" : "https://i.pinimg.com/564x/49/2a/7d/492a7d30875b68c32478a8595dc9ccc2.jpg" },
  { "name" : "Kumari Aashi", "rollNo" : 22015318, "imgSrc" : "https://i.pinimg.com/564x/f0/d2/eb/f0d2eb3fc8c39d8671b46486bc256617.jpg" },
  { "name" : "KUNAL PRASAD", "rollNo" : 22015319, "imgSrc" : "https://i.pinimg.com/564x/34/52/a3/3452a32cab9e76f0c813afe1dc01f88e.jpg" },
  { "name" : "LOKESH KUMAR GHRITLAHARE", "rollNo" : 22015320, "imgSrc" : "https://i.pinimg.com/564x/3a/8c/d5/3a8cd52af76df7e2076170a9e2099911.jpg" },
  { "name" : "MADHU DUBEY", "rollNo" : 22015321, "imgSrc" : "https://i.pinimg.com/736x/a9/6a/ab/a96aab16392aca70f43f62e35c674019.jpg" },
  { "name" : "MAHIMA NETAM", "rollNo" : 22015322, "imgSrc" : "https://i.pinimg.com/564x/1c/e0/e0/1ce0e0ae6717698e87954d2d15cd4e08.jpg" },
  { "name" : "MAYANK SAIYAM", "rollNo" : 22015323, "imgSrc" : "https://i.pinimg.com/564x/47/31/a0/4731a090c360c5bc289476d37a046877.jpg" },
  { "name" : "Muskan Gupta", "rollNo" : 22015324, "imgSrc" : "https://i.pinimg.com/564x/19/b7/5a/19b75ad01069b93a5d19bb9f0f12fdaf.jpg" },
  { "name" : "OMKAR NAYAK", "rollNo" : 22015325, "imgSrc" : "https://i.pinimg.com/564x/00/b3/70/00b3709837e9f6fbcdac3faeba2de4ae.jpg" },
  { "name" : "OMKAR PRASAD DHRUW", "rollNo" : 22015326, "imgSrc" : "https://i.pinimg.com/564x/4f/95/00/4f9500200a1ccd54fc29e76c5bcc1694.jpg" },
  { "name" : "PARASMANI KHUNTE", "rollNo" : 22015327, "imgSrc" : "https://i.pinimg.com/736x/6a/e8/27/6ae827fcca32bf53c2a286efeb0b145d.jpg" },
  { "name" : "Prabhanshu kerketta", "rollNo" : 22015328, "imgSrc" : "https://i.pinimg.com/564x/f0/b6/50/f0b6502e50606b96759d13d84e10f674.jpg" },
  { "name" : "Pratik Mukherjee", "rollNo" : 22015329, "imgSrc" : "https://i.pinimg.com/originals/ff/16/92/ff169223e8e602d2db1a412379425df8.gif" },
  { "name" : "Rahul Nishad", "rollNo" : 22015330, "imgSrc" : "https://i.pinimg.com/736x/69/3a/3f/693a3faf19e9e58c534ca2d4630e2926.jpg" },
  { "name" : "rishabh jogi", "rollNo" : 22015332, "imgSrc" : "https://i.pinimg.com/564x/7b/c5/50/7bc5504281bf11e07eb2009cbd3e53a4.jpg" },
  { "name" : "Rishabh Vaishnav", "rollNo" : 22015333, "imgSrc" : "https://i.pinimg.com/564x/de/e2/e1/dee2e1e59939b9075a486556aa323f7b.jpg" },
  { "name" : "RIYA SINGH", "rollNo" : 22015334, "imgSrc" : "https://i.pinimg.com/736x/3b/19/fc/3b19fc0712d259dfafcfc2c140b8d04b.jpg" },
  { "name" : "Sagar Singh", "rollNo" : 22015335, "imgSrc" : "https://i.pinimg.com/originals/3a/0b/93/3a0b93b4bb41b7fffb59c46ef21f2691.gif" },
  { "name" : "SAKSHAM SHRIVASTAVA", "rollNo" : 22015336, "imgSrc" : "https://i.pinimg.com/564x/be/6f/05/be6f058e937d22df7f1a7f2754513602.jpg" },
  { "name" : "SARTHAK BHAGAT", "rollNo" : 22015337, "imgSrc" : "https://i.pinimg.com/564x/c5/c5/0b/c5c50b69abcce0b501a3dbe97e001367.jpg" },
  { "name" : "SAURABH KUMAR YADAW", "rollNo" : 22015339, "imgSrc" : "https://i.pinimg.com/564x/7a/7c/b7/7a7cb7c7770ecdb84fc3e72b0b62d685.jpg" },
  { "name" : "SAURABH MAURYA", "rollNo" : 22015340, "imgSrc" : "https://i.pinimg.com/564x/75/e6/55/75e65535251314ade927ab59636d1e3f.jpg" },
  { "name" : "SHREYA SINGH", "rollNo" : 22015341, "imgSrc" : "https://i.pinimg.com/564x/93/ec/ff/93ecffb0207084e44a9ab3f674c1b6c5.jpg" },
  { "name" : "SHUBHAM CHANDRAKAR", "rollNo" : 22015342, "imgSrc" : "https://i.pinimg.com/564x/45/97/58/459758e448a26ecf91d3334970720a98.jpg" },
  { "name" : "SHUBHAM SINGH", "rollNo" : 22015343, "imgSrc" : "https://i.pinimg.com/736x/ed/c3/4c/edc34cefdb9247c37a037a3635d9e98c.jpg" },
  { "name" : "SONAL DHRUW", "rollNo" : 22015344, "imgSrc" : "https://i.pinimg.com/736x/a1/1e/b6/a11eb6bc6cbeb22169cb97ffce84782a.jpg" },
  { "name" : "SRISHTY JHA", "rollNo" : 22015345, "imgSrc" : "https://i.pinimg.com/564x/5e/fd/52/5efd52ee4ca00727e763bf0968627e00.jpg" },
  { "name" : "SUJAL ADITYA MINJ", "rollNo" : 22015346, "imgSrc" : "https://i.pinimg.com/736x/f7/0e/d8/f70ed8f9327b7df7d87693a34b8d650f.jpg" },
  { "name" : "Sushil Patel", "rollNo" : 22015347, "imgSrc" : "https://i.pinimg.com/736x/e8/d2/47/e8d247c0ecbb6375efbfc7d5cadf6892.jpg" },
  { "name" : "TEJ PRATAP SHARMA", "rollNo" : 22015348, "imgSrc" : "https://i.pinimg.com/564x/d4/75/4f/d4754f9205f20c2ffb52d9d0b615c36e.jpg" },
  { "name" : "TRIPURARI NATH", "rollNo" : 22015349, "imgSrc" : "https://i.pinimg.com/736x/1c/20/7c/1c207c7be2861d33f75fba2126d245ca.jpg" },
  { "name" : "VAIBHAV KHARE", "rollNo" : 22015350, "imgSrc" : "https://i.pinimg.com/564x/f0/30/79/f03079bce7684cb64bcd1e77d0b8062e.jpg" },
  { "name" : "VARUN KAIWART", "rollNo" : 22015351, "imgSrc" : "https://i.pinimg.com/564x/d9/21/60/d92160da86a546289978a4d589e434bf.jpg" },
]


# version 1

# for student in names:
#     print(f"Name: {student['name']}")
#     print(f"Roll Number: {student['rollNo']}")
#     print(f"Image Source: {student['imgSrc']}")
#     print("-" * 20)  # Optional separator between students


# version 2 

# class StudentViewer(tk.Frame):
#     def __init__(self, master, students):
#         super().__init__(master)
#         self.master = master
#         self.students = students
#         self.current_index = 0
        
#         self.name_label = tk.Label(self, text="")
#         self.name_label.pack()

#         self.rollno_label = tk.Label(self, text="")
#         self.rollno_label.pack()

#         self.img_label = tk.Label(self)
#         self.img_label.pack()

#         self.prev_button = tk.Button(self, text="Previous", command=self.show_previous)
#         self.prev_button.pack(side=tk.LEFT)

#         self.next_button = tk.Button(self, text="Next", command=self.show_next)
#         self.next_button.pack(side=tk.RIGHT)
        
#         self.pack()
#         self.show_student()

#     def show_student(self):
#         student = self.students[self.current_index]
#         self.name_label.config(text=f"Name: {student['name']}")
#         self.rollno_label.config(text=f"Roll Number: {student['rollNo']}")

#         response = requests.get(student['imgSrc'])
#         img_data = response.content
#         img = Image.open(BytesIO(img_data))
#         img = img.resize((100, 100), Image.LANCZOS)
#         img = ImageTk.PhotoImage(img)
        
#         self.img_label.config(image=img)
#         self.img_label.image = img

#     def show_previous(self):
#         if self.current_index > 0:
#             self.current_index -= 1
#             self.show_student()

#     def show_next(self):
#         if self.current_index < len(self.students) - 1:
#             self.current_index += 1
#             self.show_student()

# root = tk.Tk()
# root.title("Student Information")

# app = StudentViewer(root, names)

# root.mainloop()


#version 3

# class StudentViewer(tk.Frame):
#     def __init__(self, master, students):
#         super().__init__(master)
#         self.master = master
#         self.students = students
#         self.current_index = 0
#         self.attendance = {}

#         self.master.geometry("600x500")
        
#         self.name_label = tk.Label(self, text="")
#         self.name_label.pack()

#         self.rollno_label = tk.Label(self, text="")
#         self.rollno_label.pack()

#         self.img_label = tk.Label(self)
#         self.img_label.pack()

#         self.attendance_var = tk.StringVar(value="Absent")
#         self.absent_radio = tk.Radiobutton(self, text="Absent", variable=self.attendance_var, value="Absent")
#         self.absent_radio.pack()
#         self.present_radio = tk.Radiobutton(self, text="Present", variable=self.attendance_var, value="Present")
#         self.present_radio.pack()

#         self.prev_button = tk.Button(self, text="Previous", command=self.show_previous)
#         self.prev_button.pack(side=tk.LEFT)

#         self.next_button = tk.Button(self, text="Next", command=self.show_next)
#         self.next_button.pack(side=tk.RIGHT)
        
#         self.submit_button = tk.Button(self, text="Submit", command=self.submit)
#         self.submit_button.pack(side=tk.BOTTOM)
#         self.submit_button.pack_forget()  # Hide the submit button initially

#         self.pack()
#         self.show_student()

#     def show_student(self):
#         student = self.students[self.current_index]
#         self.name_label.config(text=f"Name: {student['name']}")
#         self.rollno_label.config(text=f"Roll Number: {student['rollNo']}")

#         response = requests.get(student['imgSrc'])
#         img_data = response.content
#         img = Image.open(BytesIO(img_data))
#         img = img.resize((100, 100), Image.LANCZOS)
#         img = ImageTk.PhotoImage(img)
        
#         self.img_label.config(image=img)
#         self.img_label.image = img

#         self.attendance_var.set(self.attendance.get(student['rollNo'], "Absent"))

#     def show_previous(self):
#         if self.current_index > 0:
#             self.current_index -= 1
#             self.show_student()
#         self.submit_button.pack_forget()

#     def show_next(self):
#         self.attendance[self.students[self.current_index]['rollNo']] = self.attendance_var.get()
#         if self.current_index < len(self.students) - 1:
#             self.current_index += 1
#             self.show_student()
#         if self.current_index == len(self.students) - 1:
#             self.submit_button.pack(side=tk.BOTTOM)

#     def submit(self):
#         self.attendance[self.students[self.current_index]['rollNo']] = self.attendance_var.get()
#         present_students = []
#         absent_students = []
#         for student in self.students:
#             if self.attendance[student['rollNo']] == "Present":
#                 present_students.append(student)
#             else:
#                 absent_students.append(student)
#         self.show_results(present_students, absent_students)

#     def show_results(self, present_students, absent_students):
#         results_window = tk.Toplevel(self.master)
#         results_window.title("Attendance Results")
#         results_window.geometry("800x600")

#         present_label = tk.Label(results_window, text="Present Students", font=("Arial", 16))
#         present_label.pack()

#         present_tree = ttk.Treeview(results_window, columns=("Name", "Roll No", "Photo"), show="headings")
#         present_tree.heading("Name", text="Name")
#         present_tree.heading("Roll No", text="Roll No")
#         present_tree.heading("Photo", text="Photo")
#         present_tree.pack()

#         for student in present_students:
#             present_tree.insert("", tk.END, values=(student['name'], student['rollNo'], student['imgSrc']))

#         absent_label = tk.Label(results_window, text="Absent Students", font=("Arial", 16))
#         absent_label.pack()

#         absent_tree = ttk.Treeview(results_window, columns=("Name", "Roll No", "Photo"), show="headings")
#         absent_tree.heading("Name", text="Name")
#         absent_tree.heading("Roll No", text="Roll No")
#         absent_tree.heading("Photo", text="Photo")
#         absent_tree.pack()

#         for student in absent_students:
#             absent_tree.insert("", tk.END, values=(student['name'], student['rollNo'], student['imgSrc']))

#         def save_to_excel():
#             data = {
#                 "Present Students": present_students,
#                 "Absent Students": absent_students
#             }
#             writer = pd.ExcelWriter('attendance.xlsx', engine='openpyxl')

#             for status, students in data.items():
#                 df = pd.DataFrame(students)
#                 df.to_excel(writer, sheet_name=status, index=False)

#             writer.save()
#             messagebox.showinfo("Success", "Attendance data saved to attendance.xlsx")

#         save_button = tk.Button(results_window, text="Save to Excel", command=save_to_excel)
#         save_button.pack()

# root = tk.Tk()
# root.title("Student Information")

# app = StudentViewer(root, names)

# root.mainloop()


#version 4


class StudentViewer(tk.Frame):
    def __init__(self, master, students):
        super().__init__(master)
        self.master = master
        self.students = students
        self.current_index = 0
        self.attendance = {}

        self.master.geometry("800x600")
        self.master.config(bg="#2980b9")

        style = ttk.Style()
        style.configure("TLabel", foreground="black", font=("Helvetica", 12))
        style.configure("TButton", foreground="black", font=("Helvetica", 12))
        style.configure("TRadiobutton", foreground="black", font=("Helvetica", 12))

        self.name_label = ttk.Label(self, text="")
        self.name_label.pack(pady=20)

        self.rollno_label = ttk.Label(self, text="")
        self.rollno_label.pack(pady=20)

        self.img_label = ttk.Label(self)
        self.img_label.pack(pady=20)

        self.attendance_var = tk.StringVar(value="Absent")
        self.absent_radio = ttk.Radiobutton(self, text="Absent", variable=self.attendance_var, value="Absent")
        self.absent_radio.pack()
        self.present_radio = ttk.Radiobutton(self, text="Present", variable=self.attendance_var, value="Present")
        self.present_radio.pack()

        self.prev_button = ttk.Button(self, text="Previous", command=self.show_previous)
        self.prev_button.pack(side=tk.LEFT, padx=50)

        self.next_button = ttk.Button(self, text="Next", command=self.show_next)
        self.next_button.pack(side=tk.RIGHT, padx=50)
        
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack(side=tk.BOTTOM, pady=50)
        self.submit_button.pack_forget()  # Hide the submit button initially

        self.pack(pady=50)
        self.show_student()

    def show_student(self):
        student = self.students[self.current_index]
        self.name_label.config(text=f"Name: {student['name']}")
        self.rollno_label.config(text=f"Roll Number: {student['rollNo']}")

        response = requests.get(student['imgSrc'])
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((250, 250), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        self.img_label.config(image=img)
        self.img_label.image = img

        self.attendance_var.set(self.attendance.get(student['rollNo'], "Absent"))

    def show_previous(self):
        if self.current_index > 0:
            self.attendance[self.students[self.current_index]['rollNo']] = self.attendance_var.get()
            self.current_index -= 1
            self.show_student()
        self.submit_button.pack_forget()

    def show_next(self):
        self.attendance[self.students[self.current_index]['rollNo']] = self.attendance_var.get()
        if self.current_index < len(self.students) - 1:
            self.current_index += 1
            self.show_student()
        if self.current_index == len(self.students) - 1:
            self.submit_button.pack(side=tk.BOTTOM, pady=20)

    def submit(self):
        self.attendance[self.students[self.current_index]['rollNo']] = self.attendance_var.get()
        present_students = []
        absent_students = []
        for student in self.students:
            if self.attendance[student['rollNo']] == "Present":
                present_students.append(student)
            else:
                absent_students.append(student)
        self.show_results(present_students, absent_students)

    def show_results(self, present_students, absent_students):
        results_window = tk.Toplevel(self.master)
        results_window.title("Attendance Results")
        results_window.geometry("800x600")
        results_window.config(bg="#2c3e50")

        present_label = ttk.Label(results_window, text="Present Students", font=("Arial", 16), foreground="black")
        present_label.pack(pady=10)

        present_tree = ttk.Treeview(results_window, columns=("Name", "Roll No", "Photo"), show="headings")
        present_tree.heading("Name", text="Name")
        present_tree.heading("Roll No", text="Roll No")
        present_tree.heading("Photo", text="Photo")
        present_tree.pack(pady=10)

        for student in present_students:
            present_tree.insert("", tk.END, values=(student['name'], student['rollNo'], student['imgSrc']))

        absent_label = ttk.Label(results_window, text="Absent Students", font=("Arial", 16), foreground="black")
        absent_label.pack(pady=10)

        absent_tree = ttk.Treeview(results_window, columns=("Name", "Roll No", "Photo"), show="headings")
        absent_tree.heading("Name", text="Name")
        absent_tree.heading("Roll No", text="Roll No")
        absent_tree.heading("Photo", text="Photo")
        absent_tree.pack(pady=10)

        for student in absent_students:
            absent_tree.insert("", tk.END, values=(student['name'], student['rollNo'], student['imgSrc']))

        def save_to_excel():
            data = {
                "Present Students": present_students,
                "Absent Students": absent_students
            }
            writer = pd.ExcelWriter('attendance.xlsx', engine='openpyxl')

            for status, students in data.items():
                df = pd.DataFrame(students)
                df.to_excel(writer, sheet_name=status, index=False)

            writer._save()
            messagebox.showinfo("Success", "Attendance data saved to attendance.xlsx")

        save_button = ttk.Button(results_window, text="Save to Excel", command=save_to_excel)
        save_button.pack(pady=20)

root = tk.Tk()
root.title("Student Information")

app = StudentViewer(root, names)

root.mainloop()