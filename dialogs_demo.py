"""
dialogs_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    Two families of pop-up dialog that come with tkinter:
        - messagebox: show info / warnings, and ask yes/no questions.
        - filedialog: let the user CHOOSE which file to open or save.

    filedialog is the GUI-native key to file persistence -- it returns the path
    the user picked, which you then open() as usual. Files are opened with
    encoding="utf-8" so that macrons (a e i o u with macrons) save correctly.

HOW TO RUN
    python dialogs_demo.py
"""

import tkinter as tk
from tkinter import messagebox, filedialog


def main():
    root = tk.Tk()
    root.title("Dialogs demo")
    root.geometry("420x260")

    textbox = tk.Text(root, height=8, width=46, wrap="word")
    textbox.pack(padx=10, pady=10)
    textbox.insert("1.0", "Type something, then use Save to write it to a file.")

    # --- messagebox --------------------------------------------------------
    def about():
        messagebox.showinfo("About", "A tiny dialogs demo.")

    def confirm_clear():
        # askyesno returns True/False -- use it to confirm destructive actions.
        if messagebox.askyesno("Clear", "Erase all the text?"):
            textbox.delete("1.0", tk.END)

    # --- filedialog + file I/O ---------------------------------------------
    def save_as():
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt")])
        if not path:                 # user pressed Cancel -> path is "" -> stop
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write(textbox.get("1.0", tk.END))
        messagebox.showinfo("Saved", f"Saved to:\n{path}")

    def open_file():
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not path:
            return
        with open(path, encoding="utf-8") as f:
            textbox.delete("1.0", tk.END)
            textbox.insert("1.0", f.read())

    bar = tk.Frame(root)
    bar.pack()
    tk.Button(bar, text="Open", command=open_file).pack(side="left", padx=4)
    tk.Button(bar, text="Save as", command=save_as).pack(side="left", padx=4)
    tk.Button(bar, text="Clear", command=confirm_clear).pack(side="left", padx=4)
    tk.Button(bar, text="About", command=about).pack(side="left", padx=4)

    root.mainloop()


if __name__ == "__main__":
    main()
