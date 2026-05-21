"""
entry_demo.py  --  tkinter widget reference  --  Year 12 & 13 Digital Technology

WHAT THIS DEMONSTRATES
    An Entry is a single-line text box the user types into. It is the most common
    way a tkinter program takes input from the user.

    This file has TWO versions:
        run_level2()  -> reads input, VALIDATES it, and responds to events.
                         This is what AS91896 (L2) rewards: responding to GUI
                         events + using a non-core library (tkinter).
        run_level3()  -> the same idea moved INTO A CLASS, with input validation
                         AND saving to a file. That single example shows a GUI,
                         event handling, a class you defined, validation, and
                         persistent storage -- several of the AS91906 (L3)
                         complex techniques at once.

HOW TO RUN
    Press Run in VS Code, or:  python entry_demo.py
    By default it runs the Level 2 version. To try the Level 3 version, change
    the line at the bottom from run_level2() to run_level3().
"""

import tkinter as tk
from tkinter import messagebox


# ---------------------------------------------------------------------------
# LEVEL 2: read an Entry, validate it, respond to a button AND the Enter key
# ---------------------------------------------------------------------------
def run_level2():
    window = tk.Tk()
    window.title("Entry demo (Level 2)")
    window.geometry("340x200")

    tk.Label(window, text="Enter your name:").pack(pady=(16, 4))

    # Link the Entry to a StringVar so we can read its value cleanly.
    name_var = tk.StringVar()
    entry = tk.Entry(window, textvariable=name_var, width=28)
    entry.pack(pady=4)
    entry.focus()  # cursor starts in the box -- a small usability touch

    result = tk.Label(window, text="", font=("TkDefaultFont", 12))
    result.pack(pady=12)

    def greet(event=None):           # event=None lets BOTH the button and a key call it
        name = name_var.get().strip()  # .get() ALWAYS returns a string
        if not name:                   # validation: reject empty / whitespace input
            messagebox.showwarning("Missing name", "Please type your name first.")
            return
        result.config(text=f"Kia ora, {name}!")

    tk.Button(window, text="Greet", command=greet).pack()

    # Respond to an event from the keyboard: pressing Enter inside the Entry.
    entry.bind("<Return>", greet)

    window.mainloop()


# ---------------------------------------------------------------------------
# LEVEL 3 LIFT: same widget, now inside a class, with validation + persistence
# ---------------------------------------------------------------------------
class NameApp:
    """A small class-based app that saves validated names to a file.

    This demonstrates, in one place:
        - writing code for a GUI            (complex technique)
        - a class/object you defined        (complex technique)
        - reading/writing persistent storage(complex technique)
        - input validation                  (makes the program robust)
    """

    FILE = "names.txt"

    def __init__(self, root):
        self.root = root
        self.root.title("Entry demo (Level 3)")
        self.root.geometry("340x220")

        self.name_var = tk.StringVar()

        tk.Label(root, text="Enter a name to save:").pack(pady=(16, 4))
        entry = tk.Entry(root, textvariable=self.name_var, width=28)
        entry.pack(pady=4)
        entry.focus()
        entry.bind("<Return>", lambda event: self.save())

        tk.Button(root, text="Save", command=self.save).pack(pady=8)
        self.status = tk.Label(root, text="", fg="#0F6E56")
        self.status.pack(pady=8)

    def save(self):
        name = self.name_var.get().strip()
        if not name:                                   # validation
            messagebox.showwarning("Missing name", "Please type a name first.")
            return
        with open(self.FILE, "a", encoding="utf-8") as f:  # persistent storage
            f.write(name + "\n")
        self.status.config(text=f'Saved "{name}" to {self.FILE}')
        self.name_var.set("")                           # clear ready for the next one


def run_level3():
    root = tk.Tk()
    NameApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_level2()
    # To try the Level 3 version instead, comment out the line above and use:
    # run_level3()
