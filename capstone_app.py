"""
capstone_app.py  --  tkinter widget reference  --  Year 13 (Level 3)

WHAT THIS DEMONSTRATES
    A small but complete program that pulls several widgets together the way a
    real project does. It is the bridge from "I can use a widget" to "I can build
    a complex outcome", and it shows MANY of the named complex techniques at once:

        - writing code for a GUI                         (complex technique)
        - a class/object you defined                     (complex technique)
        - reading from / writing to persistent storage   (complex technique)
        - a non-core library (tkinter / json)            (complex technique)
        - modifying data held in a collection            (advanced technique)
        - input validation + handling the empty/invalid case (robustness)

    The program: a simple student record manager. Add a name, year and grade;
    the records show in a table; everything is saved to a JSON file and reloaded
    next time you open the program.

HOW TO RUN
    python capstone_app.py
"""

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox


class RecordManager:
    FILE = "records.json"
    GRADES = ["Not Achieved", "Achieved", "Merit", "Excellence"]

    def __init__(self, root):
        self.root = root
        self.root.title("Student records")
        self.root.geometry("520x360")

        self.records = []            # the collection we add to / save / load
        self._build_menu()
        self._build_form()
        self._build_table()
        self.load()                  # restore previous data on startup

    # ---- interface -------------------------------------------------------
    def _build_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save now", command=self.save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def _build_form(self):
        form = tk.Frame(self.root, padx=10, pady=10)
        form.pack(fill="x")

        tk.Label(form, text="Name").grid(row=0, column=0, padx=4)
        tk.Label(form, text="Year").grid(row=0, column=1, padx=4)
        tk.Label(form, text="Grade").grid(row=0, column=2, padx=4)

        self.name_var = tk.StringVar()
        self.year_var = tk.IntVar(value=12)
        self.grade_var = tk.StringVar(value=self.GRADES[1])

        tk.Entry(form, textvariable=self.name_var, width=18).grid(row=1, column=0, padx=4)
        ttk.Combobox(form, textvariable=self.year_var, width=5, state="readonly",
                     values=[9, 10, 11, 12, 13]).grid(row=1, column=1, padx=4)
        ttk.Combobox(form, textvariable=self.grade_var, width=14, state="readonly",
                     values=self.GRADES).grid(row=1, column=2, padx=4)

        tk.Button(form, text="Add", command=self.add).grid(row=1, column=3, padx=8)
        tk.Button(form, text="Remove selected", command=self.remove).grid(row=1, column=4)

    def _build_table(self):
        self.tree = ttk.Treeview(self.root, columns=("name", "year", "grade"),
                                 show="headings", height=10)
        for col, title, width in (("name", "Name", 200), ("year", "Year", 60),
                                  ("grade", "Grade", 140)):
            self.tree.heading(col, text=title)
            self.tree.column(col, width=width)
        self.tree.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    # ---- behaviour -------------------------------------------------------
    def add(self):
        name = self.name_var.get().strip()
        if not name:                                  # validation
            messagebox.showwarning("Missing name", "Please enter a name.")
            return
        record = {"name": name, "year": self.year_var.get(),
                  "grade": self.grade_var.get()}
        self.records.append(record)                   # modify the collection
        self._add_row(record)
        self.name_var.set("")
        self.save()

    def remove(self):
        chosen = self.tree.selection()
        if not chosen:                                # handle the empty case
            return
        index = self.tree.index(chosen[0])
        self.tree.delete(chosen[0])
        del self.records[index]
        self.save()

    def _add_row(self, record):
        self.tree.insert("", tk.END,
                         values=(record["name"], record["year"], record["grade"]))

    # ---- persistence -----------------------------------------------------
    def save(self):
        with open(self.FILE, "w", encoding="utf-8") as f:
            json.dump(self.records, f, indent=2)

    def load(self):
        if not os.path.exists(self.FILE):
            return                                    # first run: nothing to load
        try:
            with open(self.FILE, encoding="utf-8") as f:
                self.records = json.load(f)
            for record in self.records:
                self._add_row(record)
        except (json.JSONDecodeError, KeyError):
            messagebox.showwarning("Load failed", "The saved file could not be read.")
            self.records = []


if __name__ == "__main__":
    root = tk.Tk()
    RecordManager(root)
    root.mainloop()
