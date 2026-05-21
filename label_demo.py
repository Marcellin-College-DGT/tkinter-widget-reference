"""
label_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    A Label is an OUTPUT widget. It shows text (or an image) to the user.
    It does not collect input and it does not respond to events.

    There are two ways to change what a Label shows:
        1. label.config(text="...")          -> set the text directly
        2. link a StringVar and call .set()   -> the Label updates itself

    This demo shows both, plus the most common beginner task: a click counter
    that updates a Label every time a Button is pressed.

HOW TO RUN
    python label_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Label demo")
    root.geometry("320x200")

    # --- A plain, static Label ---------------------------------------------
    tk.Label(root, text="Labels show information to the user").pack(pady=(16, 4))

    # --- A Label whose text can change at run time -------------------------
    # We link the Label to a StringVar. Change the variable and the Label
    # redraws itself -- we never touch the Label again directly.
    count = 0
    status_var = tk.StringVar()
    status_var.set(f"Clicks: {count}")
    tk.Label(root, textvariable=status_var, font=("TkDefaultFont", 14)).pack(pady=8)

    # --- The event handler -------------------------------------------------
    def add_click():
        nonlocal count          # we are changing 'count' from the enclosing scope
        count += 1
        status_var.set(f"Clicks: {count}")

    # command= is set to OUR function (no brackets -- we pass it, not call it).
    tk.Button(root, text="Click me", command=add_click).pack(pady=8)

    # --- A Label that wraps long text --------------------------------------
    # By default a Label does NOT wrap. wraplength (in pixels) forces it to.
    tk.Label(root, wraplength=280, fg="#5F5E5A",
             text="Tip: a Label will not wrap long text on its own -- set wraplength."
             ).pack(pady=(8, 16))

    root.mainloop()


if __name__ == "__main__":
    main()
