"""
text_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    A Text widget holds MULTIPLE lines (unlike Entry, which holds one).
        - insert, get and delete using "line.column" indexes and tk.END
        - a live word count that updates on every key release (event binding)

HOW TO RUN
    python text_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Text demo")
    root.geometry("420x300")

    textbox = tk.Text(root, height=10, width=48, wrap="word")
    textbox.pack(padx=10, pady=10)
    textbox.insert("1.0", "Type here. This is line 1, column 0.")  # "1.0" = line 1, col 0

    count = tk.Label(root, text="Words: 0")
    count.pack()

    def update_count(event=None):
        # get() needs a start and end index. "1.0" to tk.END grabs everything.
        content = textbox.get("1.0", tk.END)
        count.config(text=f"Words: {len(content.split())}")

    # <KeyRelease> fires after each keypress, so the count stays current.
    textbox.bind("<KeyRelease>", update_count)

    def clear():
        textbox.delete("1.0", tk.END)   # delete from start to end
        update_count()

    tk.Button(root, text="Clear", command=clear).pack(pady=6)

    update_count()
    root.mainloop()


if __name__ == "__main__":
    main()
