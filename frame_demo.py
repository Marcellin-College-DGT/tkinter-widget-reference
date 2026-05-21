"""
frame_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    A Frame is an invisible container that GROUPS widgets. The most useful thing
    Frames let you do is COMBINE layout managers safely.

    The rule: use ONE manager per container -- never mix pack and grid in the
    same container (tkinter will hang). But every Frame is its own container, so
    you can give each Frame the manager that fits it:

        - the toolbar is a linear row        -> pack
        - the form is rows and columns       -> grid
        - each labelled field is a mini-row  -> pack (inside its own frame)

    This one window shows pack and grid working together, each in its own Frame,
    plus a reusable Frame SUBCLASS (a Level 3 idea: defining your own class).

HOW TO RUN
    python frame_demo.py
"""

import tkinter as tk


# A reusable component made by subclassing Frame. Inside its OWN frame it uses
# pack -- which is fine, because it is a separate container from the form.
class LabelledEntry(tk.Frame):
    def __init__(self, parent, caption):
        super().__init__(parent)
        tk.Label(self, text=caption, width=7, anchor="e").pack(side="left")
        self.var = tk.StringVar()
        tk.Entry(self, textvariable=self.var, width=18).pack(side="left")

    def value(self):
        return self.var.get()


def main():
    root = tk.Tk()
    root.title("Frame demo: pack + grid together")
    root.geometry("420x230")

    # --- TOOLBAR -- a single horizontal row, so PACK is the natural fit. -----
    # This Frame is its own container; everything inside it is packed.
    toolbar = tk.Frame(root, bd=1, relief="solid")
    toolbar.pack(side="top", fill="x", padx=8, pady=8)
    for label in ("New", "Open", "Save"):
        tk.Button(toolbar, text=label).pack(side="left", padx=2, pady=4)

    # --- FORM -- rows and columns, so GRID is the natural fit. ---------------
    # A DIFFERENT container, so using grid here does NOT clash with the packed
    # toolbar above. One manager per container is the whole trick.
    form = tk.Frame(root, padx=8, pady=8)
    form.pack(side="top", fill="both", expand=True)

    first = LabelledEntry(form, "First:")
    first.grid(row=0, column=0, sticky="w", pady=3)     # the LabelledEntry frame is GRIDDED here
    last = LabelledEntry(form, "Last:")
    last.grid(row=1, column=0, sticky="w", pady=3)

    result = tk.Label(form, text="", fg="#0F6E56")
    result.grid(row=2, column=0, sticky="w", pady=8)

    def greet():
        result.config(text=f"Kia ora, {first.value()} {last.value()}".strip())

    tk.Button(form, text="Greet", command=greet).grid(row=3, column=0, sticky="w")

    root.mainloop()


if __name__ == "__main__":
    main()
