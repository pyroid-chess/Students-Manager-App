# 🎓 Students Manager

**Students Manager** is a simple educational project built with **Python**.  
Its main purpose is to **manage a student group** with a clean graphical user interface (GUI) using `tkinter`.  
This project demonstrates basic CRUD operations for managing students and shows how to integrate traditional Python logic with a GUI.

---

## 📌 Project Description

- **Name:** Students Manager
- **Type:** Python GUI Application
- **Purpose:** Add, remove, check, display, and clear students easily through an intuitive GUI.
- **Original Logic:** Created by `youcefshaaban`.
- **GUI Integration:** Implemented with `tkinter` and enhanced by ChatGPT.

---

## ⚙️ Available Functions

| Function           | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `add_student()`    | Add a new student to the list                             |
| `remove_student()` | Remove a selected student from the list                   |
| `check_student()`  | Check if a student exists in the list                     |
| `show_students()`  | Display all students (managed via the listbox in the GUI) |
| `clear_students()` | Clear all students from the list with confirmation        |
| `update_student()` | Update an existing student to a new name                  |

---

## 💾 Data Persistence (Updated)

**How does it store the data?**

- ✅ This project now uses **persistent file-based storage** using Python's built-in `pickle` module.
- ✅ All student data is saved to a file named `students_data.pkl`.
- ✅ Every time you add, remove, update, or clear students, the data is automatically saved.
- ✅ When the app is launched, it **loads the previous student list from the file**, if available.
- ❗ If the file is missing or corrupted, a new empty list will be created.

This makes the app usable beyond a single session, while still being easy to run and understand.

---

## ✅ Requirements

To run this project, you need:

- **Python 3.7+**
- Standard Python library only:
  - `tkinter` (usually bundled with Python)
  - `pickle` (built-in)
  - `os` (built-in)

No third-party packages required.

---

## 🖥️ Supported Operating Systems

This project runs on:

- ✅ **Windows** (tested)
- ✅ **Linux** (tested)
- ✅ **macOS** (should work as long as `tkinter` is installed)

---

## 🚀 How to Run

```bash
# 1️⃣ Make sure you have Python installed:
python --version

# 2️⃣ Run the Python file:
python app.py
