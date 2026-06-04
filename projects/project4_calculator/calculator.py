import tkinter as tk

# ─────────────────────────────────────────
#  CALCULATOR LOGIC
# ─────────────────────────────────────────

def button_click(value):
    """Append a digit or operator to the display."""
    current = display_var.get()
    display_var.set(current + value)


def button_clear():
    """Clear the entire display."""
    display_var.set("")


def button_backspace():
    """Delete the last character."""
    current = display_var.get()
    display_var.set(current[:-1])


def button_equal():
    """Evaluate the expression in the display."""
    expression = display_var.get()
    try:
        # Replace the display '÷' and '×' symbols with Python operators
        expression = expression.replace("÷", "/").replace("×", "*")
        result = eval(expression)          # evaluate the math expression
        # Show int if result is a whole number (e.g. 4.0 → 4)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        display_var.set(str(result))
    except ZeroDivisionError:
        display_var.set("Error: ÷ by 0")
    except Exception:
        display_var.set("Error")


# ─────────────────────────────────────────
#  WINDOW SETUP
# ─────────────────────────────────────────

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# ─────────────────────────────────────────
#  DISPLAY
# ─────────────────────────────────────────

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Courier", 28, "bold"),
    bg="#2a2a3d",
    fg="#cdd6f4",
    insertbackground="#cdd6f4",   # cursor color
    bd=0,
    relief="flat",
    justify="right",
    state="readonly"              # user cannot type directly; only buttons work
)
display.grid(row=0, column=0, columnspan=4, padx=16, pady=(16, 8), ipady=18, sticky="ew")

# ─────────────────────────────────────────
#  BUTTON FACTORY
# ─────────────────────────────────────────

def make_button(parent, text, row, col,
                cmd=None, colspan=1,
                bg="#313244", fg="#cdd6f4",
                active_bg="#585b70"):
    """Create and grid a styled button."""
    btn = tk.Button(
        parent,
        text=text,
        font=("Courier", 18, "bold"),
        bg=bg,
        fg=fg,
        activebackground=active_bg,
        activeforeground=fg,
        bd=0,
        relief="flat",
        cursor="hand2",
        command=cmd
    )
    btn.grid(
        row=row, column=col,
        columnspan=colspan,
        padx=6, pady=6,
        ipady=14, ipadx=10,
        sticky="ew"
    )
    return btn

# Row 1 — Clear, Backspace, Divide, Multiply
make_button(root, "AC",  1, 0, cmd=button_clear,                bg="#f38ba8", fg="#1e1e2e", active_bg="#eb6c8a")
make_button(root, "⌫",   1, 1, cmd=button_backspace,            bg="#fab387", fg="#1e1e2e", active_bg="#e8956f")
make_button(root, "÷",   1, 2, cmd=lambda: button_click("÷"),   bg="#89b4fa", fg="#1e1e2e", active_bg="#6b9fe0")
make_button(root, "×",   1, 3, cmd=lambda: button_click("×"),   bg="#89b4fa", fg="#1e1e2e", active_bg="#6b9fe0")

# Row 2 — 7 8 9 −
make_button(root, "7",   2, 0, cmd=lambda: button_click("7"))
make_button(root, "8",   2, 1, cmd=lambda: button_click("8"))
make_button(root, "9",   2, 2, cmd=lambda: button_click("9"))
make_button(root, "−",   2, 3, cmd=lambda: button_click("-"),   bg="#89b4fa", fg="#1e1e2e", active_bg="#6b9fe0")

# Row 3 — 4 5 6 +
make_button(root, "4",   3, 0, cmd=lambda: button_click("4"))
make_button(root, "5",   3, 1, cmd=lambda: button_click("5"))
make_button(root, "6",   3, 2, cmd=lambda: button_click("6"))
make_button(root, "+",   3, 3, cmd=lambda: button_click("+"),   bg="#89b4fa", fg="#1e1e2e", active_bg="#6b9fe0")

# Row 4 — 1 2 3 (= spans 2 rows via a frame trick below)
make_button(root, "1",   4, 0, cmd=lambda: button_click("1"))
make_button(root, "2",   4, 1, cmd=lambda: button_click("2"))
make_button(root, "3",   4, 2, cmd=lambda: button_click("3"))

# Row 5 — 0 (wide) . =
make_button(root, "0",   5, 0, cmd=lambda: button_click("0"), colspan=2)
make_button(root, ".",   5, 2, cmd=lambda: button_click("."))

# "=" spans rows 4-5 in column 3 — use rowspan via grid directly
eq_btn = tk.Button(
    root,
    text="=",
    font=("Courier", 18, "bold"),
    bg="#a6e3a1",
    fg="#1e1e2e",
    activebackground="#89cf85",
    activeforeground="#1e1e2e",
    bd=0,
    relief="flat",
    cursor="hand2",
    command=button_equal
)
eq_btn.grid(row=4, column=3, rowspan=2, padx=6, pady=6, ipady=14, ipadx=10, sticky="nsew")

# ─────────────────────────────────────────
#  COLUMN WEIGHT (makes columns equal width)
# ─────────────────────────────────────────

for i in range(4):
    root.columnconfigure(i, weight=1)


# ─────────────────────────────────────────
#  KEYBOARD SUPPORT
# ─────────────────────────────────────────

def key_press(event):
    key = event.char
    if key in "0123456789.+-*/":
        button_click(key)
    elif key == "\r":        # Enter key
        button_equal()
    elif key == "\x08":      # Backspace key
        button_backspace()
    elif key.lower() == "c": # 'c' key clears
        button_clear()

root.bind("<Key>", key_press)

# ─────────────────────────────────────────
#  RUN
# ─────────────────────────────────────────

root.mainloop()

