"""
menu_demo.py  --  tkinter widget reference  --  Year 13 (Level 3)

WHAT THIS DEMONSTRATES
    A Menu builds the menu bar across the top of a window.
        - a menubar attached to the window with root.config(menu=...)
        - a File menu with commands, a separator, and Exit
        - menus naturally open dialogs and other windows

HOW TO RUN
    python menu_demo.py
"""

import tkinter as tk
from tkinter import messagebox


def main():
    root = tk.Tk()
    root.title("Menu demo")
    root.geometry("360x200")

    status = tk.Label(root, text="Use the menu bar above", font=("TkDefaultFont", 13))
    status.pack(pady=40)

    def new_file():
        status.config(text="New file")

    def about():
        messagebox.showinfo("About", "A menu demo.")

    # 1. Make the menu bar.
    menubar = tk.Menu(root)

    # 2. Make a drop-down menu and add items to it. tearoff=0 removes the dotted line.
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=about)

    # 3. Add the drop-downs to the bar as cascades.
    menubar.add_cascade(label="File", menu=file_menu)
    menubar.add_cascade(label="Help", menu=help_menu)

    # 4. Attach the bar to the window.
    root.config(menu=menubar)

    root.mainloop()


if __name__ == "__main__":
    main()
