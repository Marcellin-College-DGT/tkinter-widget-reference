"""
toplevel_demo.py  --  tkinter widget reference  --  Year 13 (Level 3)

WHAT THIS DEMONSTRATES
    A Toplevel is a SECOND window on top of the main one -- a settings screen,
    an "add item" dialog, an about box. Multi-window programs are one of the
    "multi-screen" complexity expectations at Level 3.
        - opening a Toplevel from the main window
        - sending a value the user typed back to the main window

HOW TO RUN
    python toplevel_demo.py
"""

import tkinter as tk

window = tk.Tk()
window.title("Toplevel demo")
window.geometry("320x160")

name_label = tk.Label(window, text="No name set", font=("TkDefaultFont", 14))
name_label.pack(pady=24)

def open_settings():
    # Create the second window.
    win = tk.Toplevel(window)
    win.title("Settings")
    win.geometry("260x130")
    win.transient(window)        # keep it above its parent
    win.grab_set()               # make it modal: block the main window until closed

    tk.Label(win, text="Your name:").pack(pady=(16, 4))
    entry = tk.Entry(win)
    entry.pack()
    entry.focus()

    def apply_and_close():
        # Update the MAIN window from inside the second window, then close it.
        name_label.config(text=f"Name: {entry.get().strip() or 'No name set'}")
        win.destroy()

    tk.Button(win, text="Save", command=apply_and_close).pack(pady=12)

tk.Button(window, text="Open settings...", command=open_settings).pack()

window.mainloop()
