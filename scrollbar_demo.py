"""
scrollbar_demo.py  --  tkinter widget reference  --  Year 13 (Level 3)

WHAT THIS DEMONSTRATES
    A Scrollbar lets the user scroll a widget whose contents overflow. The key
    idea is that the scrollbar and the widget must be wired to EACH OTHER:
        - the widget tells the scrollbar where it is   (yscrollcommand)
        - the scrollbar tells the widget where to move  (command=...yview)

HOW TO RUN
    python scrollbar_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Scrollbar demo")
    root.geometry("280x240")

    # Put the list and its scrollbar in a frame so they sit neatly together.
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame, orient="vertical")
    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)   # list -> scrollbar
    scrollbar.config(command=listbox.yview)                     # scrollbar -> list

    scrollbar.pack(side="right", fill="y")
    listbox.pack(side="left", fill="both", expand=True)

    # Add enough items to overflow the box so the scrollbar is needed.
    for i in range(1, 51):
        listbox.insert(tk.END, f"Item {i}")

    root.mainloop()


if __name__ == "__main__":
    main()
