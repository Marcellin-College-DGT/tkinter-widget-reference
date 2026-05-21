"""
scale_spinbox_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    Two ways to enter a NUMBER within a range:
        - Scale: a slider. Its command callback receives the value as a STRING.
        - Spinbox: a box with up/down arrows, bounded by from_ and to.

HOW TO RUN
    python scale_spinbox_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Scale & Spinbox demo")
    root.geometry("320x220")

    # --- Scale (slider) ----------------------------------------------------
    tk.Label(root, text="Volume").pack(pady=(14, 0))
    vol_label = tk.Label(root, text="0", font=("TkDefaultFont", 14))
    vol_label.pack()

    def on_slide(value):             # value arrives as a STRING, e.g. "37.0"
        vol_label.config(text=str(int(float(value))))

    tk.Scale(root, from_=0, to=100, orient="horizontal",
             command=on_slide, showvalue=False, length=220).pack()

    # --- Spinbox -----------------------------------------------------------
    tk.Label(root, text="Quantity (1-10)").pack(pady=(14, 0))
    qty = tk.IntVar(value=1)
    tk.Spinbox(root, from_=1, to=10, textvariable=qty, width=5).pack()

    def confirm():
        # qty.get() is already an int because we used an IntVar.
        vol_label.config(text=f"Qty {qty.get()}")

    tk.Button(root, text="Confirm quantity", command=confirm).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
