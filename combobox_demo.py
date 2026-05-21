"""
combobox_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    A Combobox (from ttk) is a dropdown the user picks one value from. It is the
    tidy alternative to a long row of Radiobuttons.
        - supplying the values list
        - state="readonly" so the user picks rather than types
        - reacting to a choice with the <<ComboboxSelected>> event

HOW TO RUN
    python combobox_demo.py
"""

import tkinter as tk
from tkinter import ttk          # Combobox lives in ttk, not the base tkinter


def main():
    root = tk.Tk()
    root.title("Combobox demo")
    root.geometry("300x180")

    tk.Label(root, text="Pick a subject").pack(pady=(16, 4))

    subject = tk.StringVar()
    combo = ttk.Combobox(
        root,
        textvariable=subject,
        values=["Digital Technology", "Hospitality", "Materials Technology"],
        state="readonly",            # readonly = choose from the list, no free typing
    )
    combo.pack(pady=4)
    combo.current(0)                 # select the first item to start

    result = tk.Label(root, text="", wraplength=260, fg="#0F6E56")
    result.pack(pady=16)

    # Fires when the user picks a different item.
    def on_pick(event):
        result.config(text=f"You chose {subject.get()}")

    combo.bind("<<ComboboxSelected>>", on_pick)

    root.mainloop()


if __name__ == "__main__":
    main()
