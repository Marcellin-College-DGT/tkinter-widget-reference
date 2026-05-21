"""
canvas_demo.py  --  tkinter widget reference  --  Year 13 (Level 3)

WHAT THIS DEMONSTRATES
    A Canvas is a blank drawing area. You place shapes, lines, and text using
    pixel coordinates (x grows right, y grows DOWN from the top-left corner).
    This demo focuses on DISPLAYING visual output -- here, a simple bar chart
    drawn from a list of numbers -- rather than game mechanics.

HOW TO RUN
    python canvas_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Canvas demo")
    root.geometry("360x300")

    canvas = tk.Canvas(root, width=340, height=240, bg="white")
    canvas.pack(padx=10, pady=10)

    # A few basic shapes. Coordinates are (x1, y1, x2, y2) corners.
    canvas.create_line(40, 200, 320, 200, width=2)          # x-axis
    canvas.create_text(180, 20, text="Marks by class", font=("TkDefaultFont", 12))

    # Draw a bar chart from data. This is the kind of visual output a Label can't do.
    data = {"12DGT": 78, "13DGT": 85, "Hosp": 64}
    x = 60
    for label, value in data.items():
        top = 200 - value * 1.6                              # taller bar = bigger value
        canvas.create_rectangle(x, top, x + 60, 200, fill="#1D9E75", outline="")
        canvas.create_text(x + 30, top - 10, text=str(value))
        canvas.create_text(x + 30, 214, text=label, font=("TkDefaultFont", 9))
        x += 100

    root.mainloop()


if __name__ == "__main__":
    main()
