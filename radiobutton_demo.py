"""
radiobutton_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    Radiobuttons let the user pick exactly ONE option from a group. The trick is
    that every button in the group shares the SAME variable -- that is what makes
    them mutually exclusive.

HOW TO RUN
    python radiobutton_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Radiobutton demo")
    root.geometry("300x220")

    tk.Label(root, text="Choose a size").pack(pady=(12, 4))

    # ONE shared variable for the whole group.
    size = tk.StringVar(value="Medium")

    for label in ("Small", "Medium", "Large"):
        tk.Radiobutton(root, text=label, variable=size, value=label).pack(anchor="w", padx=60)

    result = tk.Label(root, text="", fg="#0F6E56")
    result.pack(pady=12)

    def confirm():
        result.config(text=f"You picked: {size.get()}")

    tk.Button(root, text="Confirm", command=confirm).pack()

    # You can also react the moment the choice changes, with no button:
    size.trace_add("write", lambda *args: result.config(text=f"Selected: {size.get()}"))

    root.mainloop()


if __name__ == "__main__":
    main()
