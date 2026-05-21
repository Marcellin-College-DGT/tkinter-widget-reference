"""
listbox_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    A Listbox shows a scrollable list of items the user can select from.

    This file has TWO versions:
        run_level2()  -> add items (with validation), remove the selected item,
                         and respond to the user changing the selection.
                         Adding/removing items is "modifying data stored in a
                         collection" -- an AS91896 (L2) advanced technique -- and
                         reacting to selection is "responding to GUI events".
        run_level3()  -> the same list moved INTO A CLASS that LOADS the items
                         from a file on start and SAVES them on every change.

HOW TO RUN
    python listbox_demo.py
    Runs the Level 2 version by default. To try Level 3, swap the line at the end.
"""

import tkinter as tk
from tkinter import messagebox


# ---------------------------------------------------------------------------
# LEVEL 2: add, remove, and react to selection in a Listbox
# ---------------------------------------------------------------------------
def run_level2():
    root = tk.Tk()
    root.title("Listbox demo (Level 2)")
    root.geometry("340x320")

    tk.Label(root, text="To-do list").pack(pady=(14, 4))

    listbox = tk.Listbox(root, height=8, width=34)
    listbox.pack(pady=4)
    for item in ("Finish unit plan", "Mark Year 12 tasks", "Email whanau"):
        listbox.insert(tk.END, item)   # add an item to the END of the collection

    selected = tk.Label(root, text="Nothing selected", fg="#5F5E5A")
    selected.pack(pady=4)

    # --- Add a new item, with validation ----------------------------------
    new_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=new_var, width=26)
    entry.pack(pady=(8, 2))

    def add_item():
        text = new_var.get().strip()
        existing = listbox.get(0, tk.END)        # read the whole collection back
        if not text:                             # validation: no empty items
            messagebox.showwarning("Empty item", "Type something to add.")
            return
        if text in existing:                     # validation: no duplicates
            messagebox.showwarning("Duplicate", f'"{text}" is already on the list.')
            return
        listbox.insert(tk.END, text)
        new_var.set("")

    def remove_selected():
        # curselection() returns a TUPLE of selected indices -- it may be EMPTY.
        # Check that before indexing, or the program will crash.
        choice = listbox.curselection()
        if not choice:
            messagebox.showinfo("Nothing selected", "Click an item first.")
            return
        listbox.delete(choice[0])                # remove from the collection

    tk.Button(root, text="Add", command=add_item).pack(pady=2)
    tk.Button(root, text="Remove selected", command=remove_selected).pack(pady=2)

    # --- Respond to the selection changing ---------------------------------
    # <<ListboxSelect>> is a "virtual event" tkinter fires when the choice changes.
    def on_select(event):
        choice = listbox.curselection()
        if choice:
            selected.config(text=f"Selected: {listbox.get(choice[0])}")

    listbox.bind("<<ListboxSelect>>", on_select)

    root.mainloop()


# ---------------------------------------------------------------------------
# LEVEL 3 LIFT: a class that loads the list from a file and saves on change
# ---------------------------------------------------------------------------
class TodoApp:
    """A class-based to-do list that remembers items between runs."""

    FILE = "todo.txt"

    def __init__(self, root):
        self.root = root
        self.root.title("Listbox demo (Level 3)")
        self.root.geometry("340x300")

        tk.Label(root, text="To-do list (saved to file)").pack(pady=(14, 4))
        self.listbox = tk.Listbox(root, height=8, width=34)
        self.listbox.pack(pady=4)

        self.new_var = tk.StringVar()
        tk.Entry(root, textvariable=self.new_var, width=26).pack(pady=(8, 2))
        tk.Button(root, text="Add", command=self.add_item).pack(pady=2)
        tk.Button(root, text="Remove selected", command=self.remove_selected).pack(pady=2)

        self.load()   # fill the Listbox from the file when the app starts

    def load(self):
        try:
            with open(self.FILE, encoding="utf-8") as f:
                for line in f:
                    item = line.strip()
                    if item:
                        self.listbox.insert(tk.END, item)
        except FileNotFoundError:
            pass  # first run -- no file yet, that is fine

    def save(self):
        with open(self.FILE, "w", encoding="utf-8") as f:
            for item in self.listbox.get(0, tk.END):
                f.write(item + "\n")

    def add_item(self):
        text = self.new_var.get().strip()
        if not text or text in self.listbox.get(0, tk.END):
            messagebox.showwarning("Check item", "Empty or duplicate item.")
            return
        self.listbox.insert(tk.END, text)
        self.new_var.set("")
        self.save()

    def remove_selected(self):
        choice = self.listbox.curselection()
        if not choice:
            return
        self.listbox.delete(choice[0])
        self.save()


def run_level3():
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_level2()
    # To try the Level 3 version instead, comment out the line above and use:
    # run_level3()
