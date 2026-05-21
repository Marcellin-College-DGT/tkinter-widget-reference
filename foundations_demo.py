"""
foundations_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    The four foundations every later widget assumes:
        1. the window + mainloop  -- every program has exactly one window
        2. grid layout            -- placing widgets in rows and columns
        3. StringVar / IntVar     -- variables the GUI watches and redraws from
        4. event binding          -- making the program react to the user

HOW TO RUN
    python foundations_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()                        # 1. THE MAIN WINDOW (named root by convention)
    root.title("Foundations")
    root.geometry("360x200")

    # 3. CONTROL VARIABLES -- the GUI redraws automatically when these change.
    name_var = tk.StringVar()             # holds text
    count_var = tk.IntVar(value=0)        # holds a whole number

    # 2. GRID LAYOUT -- row/column placement. Cleaner than pack for forms.
    tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=6, pady=8)
    entry = tk.Entry(root, textvariable=name_var)
    entry.grid(row=0, column=1, padx=6, pady=8)

    greeting = tk.Label(root, text="Type your name and press Enter")
    greeting.grid(row=1, column=0, columnspan=2, pady=4)

    counter = tk.Label(root, textvariable=count_var, font=("TkDefaultFont", 16))
    counter.grid(row=2, column=0, columnspan=2, pady=4)

    tk.Button(root, text="Count +1",
              command=lambda: count_var.set(count_var.get() + 1)
              ).grid(row=3, column=0, columnspan=2, pady=6)

    # 4. EVENT BINDING -- run a function when the user presses Enter in the Entry.
    def show_greeting(event):
        greeting.config(text=f"Kia ora, {name_var.get()}!")

    entry.bind("<Return>", show_greeting)

    root.mainloop()                       # hands control to tkinter


if __name__ == "__main__":
    main()
