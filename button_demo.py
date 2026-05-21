"""
button_demo.py  --  tkinter widget reference  --  Year 12 & 13

WHAT THIS DEMONSTRATES
    A Button runs a function when clicked. This shows:
        - command= to call your function (note: NO brackets -- you pass it)
        - passing an argument to the handler with lambda
        - enabling and disabling a button at run time

HOW TO RUN
    python button_demo.py
"""

import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Button demo")
    root.geometry("320x240")

    status = tk.Label(root, text="Press a button", font=("TkDefaultFont", 13))
    status.pack(pady=16)

    # A plain handler called by command= (the function is passed, not called).
    def say_hello():
        status.config(text="Hello!")

    hello_btn = tk.Button(root, text="Say hello", command=say_hello)
    hello_btn.pack(pady=4)

    # Passing an argument: lambda lets one handler serve several buttons.
    def choose(colour):
        status.config(text=f"You chose {colour}")

    for colour in ("red", "green", "blue"):
        tk.Button(root, text=colour, command=lambda c=colour: choose(c)).pack(pady=2)
        # c=colour "captures" the current value -- without it every button would
        # send the LAST colour. This is a classic loop-and-lambda gotcha.

    # Enabling / disabling another button. A button's state is "normal" or "disabled".
    def toggle_hello():
        if str(hello_btn["state"]) == "disabled":
            hello_btn.config(state="normal")
            toggle_btn.config(text="Disable 'Say hello'")
        else:
            hello_btn.config(state="disabled")
            toggle_btn.config(text="Enable 'Say hello'")

    toggle_btn = tk.Button(root, text="Disable 'Say hello'", command=toggle_hello)
    toggle_btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
