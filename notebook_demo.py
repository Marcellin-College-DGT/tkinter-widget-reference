"""
notebook_demo.py  --  tkinter widget reference  --  Year 13 (Level 3)

WHAT THIS DEMONSTRATES
    A Notebook (from ttk) gives you TABS. Each tab is a Frame you fill with its
    own widgets -- a clean way to organise a multi-section program in one window.

HOW TO RUN
    python notebook_demo.py
"""

import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Notebook demo")
    root.geometry("360x220")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Each tab is a Frame. Build the frame, fill it, then add it to the notebook.
    home = ttk.Frame(notebook)
    tk.Label(home, text="Welcome to the home tab").pack(pady=30)
    notebook.add(home, text="Home")

    settings = ttk.Frame(notebook)
    tk.Label(settings, text="Settings live here").pack(pady=20)
    tk.Checkbutton(settings, text="Enable notifications").pack()
    notebook.add(settings, text="Settings")

    about = ttk.Frame(notebook)
    tk.Label(about, text="A small notebook demo", wraplength=300).pack(pady=30)
    notebook.add(about, text="About")

    root.mainloop()


if __name__ == "__main__":
    main()
