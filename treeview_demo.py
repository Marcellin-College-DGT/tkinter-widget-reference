"""
treeview_demo.py  --  tkinter widget reference  --  Year 13 (Level 3)

WHAT THIS DEMONSTRATES
    A Treeview (from ttk) shows records in COLUMNS -- the right widget for a table
    of data, where a Listbox only shows one column. Displaying structured records
    like this supports the "complex data structures" complex technique.
        - defining columns and headings
        - inserting rows of values
        - reading the selected row

HOW TO RUN
    python treeview_demo.py
"""

import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Treeview demo")
    root.geometry("420x260")

    # show="headings" hides the empty first "tree" column so we just see our columns.
    tree = ttk.Treeview(root, columns=("name", "year", "grade"), show="headings", height=8)
    tree.pack(padx=10, pady=10, fill="x")

    # Set up the column headings and widths.
    tree.heading("name", text="Name")
    tree.heading("year", text="Year")
    tree.heading("grade", text="Grade")
    tree.column("year", width=60, anchor="center")
    tree.column("grade", width=70, anchor="center")

    # Some records to display. In a real program these might come from a file.
    records = [
        ("Aroha", 12, "Excellence"),
        ("Ben", 13, "Merit"),
        ("Mere", 12, "Achieved"),
    ]
    for row in records:
        tree.insert("", tk.END, values=row)   # "" parent = top level

    selected = tk.Label(root, text="Click a row")
    selected.pack()

    def on_select(event):
        chosen = tree.selection()              # tuple of selected row ids (may be empty)
        if chosen:
            values = tree.item(chosen[0], "values")
            selected.config(text=f"Selected: {values[0]} (Year {values[1]})")

    tree.bind("<<TreeviewSelect>>", on_select)

    root.mainloop()


if __name__ == "__main__":
    main()
