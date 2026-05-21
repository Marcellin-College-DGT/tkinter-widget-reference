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


def main():
    root = tk.Tk()
    root.title("Toplevel demo")
    root.geometry("320x160")

    name_label = tk.Label(root, text="No name set", font=("TkDefaultFont", 14))
    name_label.pack(pady=24)

    def open_settings():
        # Create the second window. Use Toplevel, never a second tk.Tk().
        win = tk.Toplevel(root)
        win.title("Settings")
        win.geometry("260x130")
        win.transient(root)          # keep it above its parent
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

    tk.Button(root, text="Open settings...", command=open_settings).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
