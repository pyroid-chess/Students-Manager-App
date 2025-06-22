"""
Students Manager GUI
Logic Made By - youcefshaaban ©
With Tkinter GUI by ChatGPT 2025
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Scrollbar
import pickle

class StudentManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Students Manager")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        # Internal persistence (simulate file with variable)
        self._data_storage = self.load_data()

        # UI Elements
        self.create_widgets()
        self.refresh_listbox()

    def create_widgets(self):
        # Title Label
        title = tk.Label(self.master, text="Students Manager", font=("Helvetica", 24, "bold"))
        title.pack(pady=10)

        # Student Name Entry
        self.entry_var = tk.StringVar()
        entry_frame = tk.Frame(self.master)
        entry_frame.pack(pady=10)

        entry_label = tk.Label(entry_frame, text="Student Name:", font=("Helvetica", 14))
        entry_label.pack(side=tk.LEFT, padx=5)

        entry = tk.Entry(entry_frame, textvariable=self.entry_var, font=("Helvetica", 14), width=30)
        entry.pack(side=tk.LEFT, padx=5)

        # Buttons Frame
        buttons_frame = tk.Frame(self.master)
        buttons_frame.pack(pady=10)

        add_btn = tk.Button(buttons_frame, text="Add Student", command=self.add_student, width=15)
        add_btn.grid(row=0, column=0, padx=5)

        remove_btn = tk.Button(buttons_frame, text="Remove Student", command=self.remove_student, width=15)
        remove_btn.grid(row=0, column=1, padx=5)

        check_btn = tk.Button(buttons_frame, text="Check Student", command=self.check_student, width=15)
        check_btn.grid(row=0, column=2, padx=5)

        clear_btn = tk.Button(buttons_frame, text="Clear All", command=self.clear_students, width=15)
        clear_btn.grid(row=1, column=0, padx=5, pady=5)

        exit_btn = tk.Button(buttons_frame, text="Exit", command=self.master.quit, width=15)
        exit_btn.grid(row=1, column=2, padx=5, pady=5)

        # Students Listbox
        list_frame = tk.Frame(self.master)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.listbox = Listbox(list_frame, font=("Helvetica", 14), width=50, height=20)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(list_frame, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

    def add_student(self):
        name = self.entry_var.get().strip().title()
        if not name:
            messagebox.showwarning("Input Error", "Please enter a student name.")
            return
        if name in self._data_storage:
            messagebox.showinfo("Duplicate", f"{name} is already in the list.")
            return
        self._data_storage.append(name)
        self.save_data()
        self.refresh_listbox()
        self.entry_var.set("")
        messagebox.showinfo("Success", f"Student {name} added successfully.")

    def remove_student(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a student to remove.")
            return
        name = self.listbox.get(selected)
        self._data_storage.remove(name)
        self.save_data()
        self.refresh_listbox()
        messagebox.showinfo("Removed", f"Student {name} removed successfully.")

    def check_student(self):
        name = self.entry_var.get().strip().title()
        if not name:
            messagebox.showwarning("Input Error", "Please enter a student name to check.")
            return
        if name in self._data_storage:
            messagebox.showinfo("Found", f"Student {name} is in the list.")
        else:
            messagebox.showinfo("Not Found", f"Student {name} not found.")

    def clear_students(self):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all students?")
        if confirm:
            self._data_storage.clear()
            self.save_data()
            self.refresh_listbox()
            messagebox.showinfo("Cleared", "All students have been cleared.")

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for student in sorted(self._data_storage):
            self.listbox.insert(tk.END, student)

    def save_data(self):
        # Save to internal pickle in attribute
        self._data_blob = pickle.dumps(self._data_storage)

    def load_data(self):
        try:
            return pickle.loads(self._data_blob)
        except AttributeError:
            return []

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()