"""
checkbutton_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    A Checkbutton is an on/off (ticked/unticked) option. Each one is backed by a
    variable you read to find its state.
        - linking each Checkbutton to a BooleanVar
        - reading several states at once into a summary

HOW TO RUN
    python checkbutton_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Checkbutton demo")
    root.geometry("300x240")

    tk.Label(root, text="Pizza toppings").pack(pady=(12, 4))

    # A variable per option. BooleanVar holds True/False.
    toppings = {
        "Cheese": tk.BooleanVar(value=True),
        "Mushroom": tk.BooleanVar(),
        "Pineapple": tk.BooleanVar(),
    }

    for name, var in toppings.items():
        tk.Checkbutton(root, text=name, variable=var).pack(anchor="w", padx=40)

    result = tk.Label(root, text="", wraplength=260, fg="#0F6E56")
    result.pack(pady=10)

    def order():
        # Read every variable and keep the ones that are ticked.
        chosen = [name for name, var in toppings.items() if var.get()]
        result.config(text="On your pizza: " + (", ".join(chosen) if chosen else "nothing!"))

    tk.Button(root, text="Order", command=order).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
