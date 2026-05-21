"""
label_demo.py  --  tkinter widget reference  --  Year 12 & 13 Digital Technology

WHAT THIS DEMONSTRATES
    A Label is an OUTPUT widget. It shows text (or an image) to the user.
    It does not collect input and it does not respond to events.

    There are two ways to change what a Label shows:
        1. label.config(text="...")          -> set the text directly
        2. link a StringVar and call .set()   -> the Label updates itself

    This demo shows both, plus the most common beginner task: a click counter
    that updates a Label every time a Button is pressed.

HOW TO RUN
    Open this file in VS Code (with the Python extension installed) and press Run,
    or from a terminal:  python label_demo.py
    tkinter comes built in with Python -- there is nothing extra to install.
"""

import tkinter as tk


def main():
    # The main window. Every tkinter program has exactly one of these.
    window = tk.Tk()
    window.title("Label demo")
    window.geometry("320x200")  # width x height in pixels

    # --- A plain, static Label -------------------------------------------------
    # The simplest possible Label: just shows fixed text.
    title = tk.Label(window, text="Labels show information to the user")
    title.pack(pady=(16, 4))

    # --- A Label whose text can change at run time -----------------------------
    # We link the Label to a StringVar. When we change the variable, the Label
    # redraws itself automatically -- we never touch the Label again directly.
    count = 0
    status_var = tk.StringVar()
    status_var.set(f"Clicks: {count}")

    status = tk.Label(window, textvariable=status_var, font=("TkDefaultFont", 14))
    status.pack(pady=8)

    # --- The event handler -----------------------------------------------------
    # A Button does not change a Label by itself. We write a function that does
    # the work, and the Button calls it. Updating the StringVar is what makes the
    # Label change on screen.
    def add_click():
        nonlocal count          # we are changing the 'count' from the enclosing scope
        count += 1
        status_var.set(f"Clicks: {count}")

    # The Button's command= is set to OUR function (no brackets -- we are passing
    # the function, not calling it).
    button = tk.Button(window, text="Click me", command=add_click)
    button.pack(pady=8)

    # --- A Label that wraps long text ------------------------------------------
    # By default a Label does NOT wrap. wraplength (in pixels) forces it to.
    note = tk.Label(
        window,
        text="Tip: a Label will not wrap long text on its own -- set wraplength.",
        wraplength=280,
        fg="#5F5E5A",
    )
    note.pack(pady=(8, 16))

    window.mainloop()  # hands control to tkinter; the window stays open until closed


if __name__ == "__main__":
    main()
