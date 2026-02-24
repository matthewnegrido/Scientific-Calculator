import tkinter as tk
import math

mode = "rad"


def calculate():
    try:
        expression = entry.get().replace("^", "**")
        result = eval(expression, {"_builtins_": None}, {
            "sin": lambda x: math.sin(math.radians(x)) if mode == "deg" else math.sin(x),
            "cos": lambda x: math.cos(math.radians(x)) if mode == "deg" else math.cos(x),
            "tan": lambda x: math.tan(math.radians(x)) if mode == "deg" else math.tan(x),
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "pow": pow
        })
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def press(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def toggle_mode():
    global mode
    mode = "deg" if mode == "rad" else "rad"
    mode_button.config(text=mode.upper())


# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE)
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/", "sqrt("],
    ["4", "5", "6", "*", "log("],
    ["1", "2", "3", "-", "ln("],
    ["0", ".", "^", "+", "sin("],
    ["cos(", "tan(", "pi", "e", "("],
    [")", "C", "="]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            tk.Button(frame, text=btn, font=("Arial", 18),
                      command=calculate).pack(side="left", expand=True, fill="both")
        elif btn == "C":
            tk.Button(frame, text=btn, font=("Arial", 18),
                      command=clear).pack(side="left", expand=True, fill="both")
        else:
            tk.Button(frame, text=btn, font=("Arial", 18),
                      command=lambda b=btn: press(b)
                      ).pack(side="left", expand=True, fill="both")

mode_button = tk.Button(root, text="RAD", font=(
    "Arial", 16), command=toggle_mode)
mode_button.pack(fill="both", padx=10, pady=5)

root.mainloop()
