import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import os
from ttkthemes import ThemedTk

class StudentManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Management System")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        self.colors = {
            "bg": "#F0F0F0",
            "fg": "#333333",
            "accent1": "#4CAF50",
            "accent2": "#2196F3",
            "accent3": "#FFC107",
            "accent4": "#E91E63",
            "accent5": "#9C27B0"
        }

        style = ttk.Style()
        style.theme_use("default")

        style.configure("TFrame", background=self.colors["bg"])
        style.configure("TLabel", background=self.colors["bg"], foreground=self.colors["fg"])
        style.configure("TEntry", fieldbackground="white", foreground=self.colors["fg"])
        style.configure("TButton", background=self.colors["accent1"], foreground="white")
        style.map("TButton", background=[("active", self.colors["accent2"])])

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.master.quit)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_tab = ttk.Frame(self.notebook)
        self.display_tab = ttk.Frame(self.notebook)
        self.search_tab = ttk.Frame(self.notebook)
        self.update_tab = ttk.Frame(self.notebook)
        self.delete_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.create_tab, text="Create/Append")
        self.notebook.add(self.display_tab, text="Display")
        self.notebook.add(self.search_tab, text="Search")
        self.notebook.add(self.update_tab, text="Update")
        self.notebook.add(self.delete_tab, text="Delete")

        self.setup_create_tab()
        self.setup_display_tab()
        self.setup_search_tab()
        self.setup_update_tab()
        self.setup_delete_tab()

    def setup_create_tab(self):
        frame = ttk.Frame(self.create_tab, padding="20 20 20 20")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Create/Append Student Record", font=("Helvetica", 16, "bold"), foreground=self.colors["accent1"]).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(frame, text="Roll No:", foreground=self.colors["accent2"]).grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
        self.roll_entry = ttk.Entry(frame, width=30)
        self.roll_entry.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Student Name:", foreground=self.colors["accent3"]).grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
        self.name_entry = ttk.Entry(frame, width=30)
        self.name_entry.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Percentage:", foreground=self.colors["accent4"]).grid(row=3, column=0, sticky="e", padx=(0, 10), pady=5)
        self.percentage_entry = ttk.Entry(frame, width=30)
        self.percentage_entry.grid(row=3, column=1, pady=5)

        ttk.Button(frame, text="Create/Append Record", command=self.create_append_record).grid(row=4, column=0, columnspan=2, pady=20)

    def setup_display_tab(self):
        frame = ttk.Frame(self.display_tab, padding="20 20 20 20")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Display All Records", font=("Helvetica", 16, "bold"), foreground=self.colors["accent2"]).pack(pady=(0, 20))

        self.display_text = tk.Text(frame, height=20, width=70, wrap=tk.WORD, bg="white", fg=self.colors["fg"])
        self.display_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.display_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.display_text.config(yscrollcommand=scrollbar.set)

        ttk.Button(frame, text="Display All Records", command=self.display_all_records).pack(pady=20)

    def setup_search_tab(self):
        frame = ttk.Frame(self.search_tab, padding="20 20 20 20")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Search Student Record", font=("Helvetica", 16, "bold"), foreground=self.colors["accent3"]).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(frame, text="Enter Roll No to Search:", foreground=self.colors["accent4"]).grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
        self.search_entry = ttk.Entry(frame, width=30)
        self.search_entry.grid(row=1, column=1, pady=5)

        ttk.Button(frame, text="Search", command=self.search_record).grid(row=2, column=0, columnspan=2, pady=20)

        self.search_result = tk.Text(frame, height=5, width=50, wrap=tk.WORD, bg="white", fg=self.colors["fg"])
        self.search_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def setup_update_tab(self):
        frame = ttk.Frame(self.update_tab, padding="20 20 20 20")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Update Student Record", font=("Helvetica", 16, "bold"), foreground=self.colors["accent4"]).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(frame, text="Enter Roll No to Update:", foreground=self.colors["accent2"]).grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
        self.update_roll_entry = ttk.Entry(frame, width=30)
        self.update_roll_entry.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="New Percentage:", foreground=self.colors["accent3"]).grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
        self.update_percentage_entry = ttk.Entry(frame, width=30)
        self.update_percentage_entry.grid(row=2, column=1, pady=5)

        ttk.Button(frame, text="Update Record", command=self.update_record).grid(row=3, column=0, columnspan=2, pady=20)

    def setup_delete_tab(self):
        frame = ttk.Frame(self.delete_tab, padding="20 20 20 20")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Delete Student Record", font=("Helvetica", 16, "bold"), foreground=self.colors["accent5"]).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        ttk.Label(frame, text="Enter Roll No to Delete:", foreground=self.colors["accent1"]).grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
        self.delete_entry = ttk.Entry(frame, width=30)
        self.delete_entry.grid(row=1, column=1, pady=5)

        ttk.Button(frame, text="Delete Record", command=self.delete_record).grid(row=2, column=0, columnspan=2, pady=20)

    def create_append_record(self):
        roll_no = self.roll_entry.get()
        name = self.name_entry.get()
        percentage = self.percentage_entry.get()

        if not roll_no or not name or not percentage:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            roll_no = int(roll_no)
            percentage = float(percentage)
        except ValueError:
            messagebox.showerror("Error", "Invalid Roll No or Percentage!")
            return

        record = [roll_no, name, percentage]

        mode = "ab" if os.path.exists("Student.dat") else "wb"
        with open("Student.dat", mode) as f:
            pickle.dump(record, f)

        messagebox.showinfo("Success", "Record added successfully!")
        self.clear_entries()

    def display_all_records(self):
        self.display_text.delete(1.0, tk.END)
        try:
            with open("Student.dat", "rb") as f:
                while True:
                    try:
                        record = pickle.load(f)
                        self.display_text.insert(tk.END, f"Roll No: {record[0]}, Name: {record[1]}, Percentage: {record[2]:.2f}%\n\n")
                    except EOFError:
                        break
        except FileNotFoundError:
            messagebox.showerror("Error", "No records found!")

    def search_record(self):
        roll_no = self.search_entry.get()
        if not roll_no:
            messagebox.showerror("Error", "Please enter a Roll No!")
            return

        try:
            roll_no = int(roll_no)
        except ValueError:
            messagebox.showerror("Error", "Invalid Roll No!")
            return

        self.search_result.delete(1.0, tk.END)
        try:
            with open("Student.dat", "rb") as f:
                while True:
                    try:
                        record = pickle.load(f)
                        if record[0] == roll_no:
                            self.search_result.insert(tk.END, f"Roll No: {record[0]}\nName: {record[1]}\nPercentage: {record[2]:.2f}%")
                            return
                    except EOFError:
                        break
            self.search_result.insert(tk.END, "Record not found!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No records found!")

    def update_record(self):
        roll_no = self.update_roll_entry.get()
        new_percentage = self.update_percentage_entry.get()

        if not roll_no or not new_percentage:
            messagebox.showerror("Error", "Both fields are required!")
            return

        try:
            roll_no = int(roll_no)
            new_percentage = float(new_percentage)
        except ValueError:
            messagebox.showerror("Error", "Invalid Roll No or Percentage!")
            return

        try:
            with open("Student.dat", "rb+") as f:
                records = []
                while True:
                    try:
                        pos = f.tell()
                        record = pickle.load(f)
                        if record[0] == roll_no:
                            record[2] = new_percentage
                            f.seek(pos)
                            pickle.dump(record, f)
                            messagebox.showinfo("Success", "Record updated successfully!")
                            return
                    except EOFError:
                        break
            messagebox.showerror("Error", "Record not found!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No records found!")

    def delete_record(self):
        roll_no = self.delete_entry.get()

        if not roll_no:
            messagebox.showerror("Error", "Please enter a Roll No!")
            return

        try:
            roll_no = int(roll_no)
        except ValueError:
            messagebox.showerror("Error", "Invalid Roll No!")
            return

        try:
            with open("Student.dat", "rb") as f:
                records = []
                while True:
                    try:
                        record = pickle.load(f)
                        if record[0] != roll_no:
                            records.append(record)
                    except EOFError:
                        break

            with open("Student.dat", "wb") as f:
                for record in records:
                    pickle.dump(record, f)

            messagebox.showinfo("Success", "Record deleted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No records found!")

    def clear_entries(self):
        self.roll_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.percentage_entry.delete(0, tk.END)

    def show_about(self):
        about_text = "Student Management System\n\nVersion 1.0\n\nCreated by Your Name"
        messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    root = ThemedTk(theme="default")
    app = StudentManagementSystem(root)
    root.mainloop()
