import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import math

root = tk.Tk()
root.title("TriCore Terminal Engine")
root.geometry("1000x700")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("clam")

header = tk.Label(
    root,
    text="TriCore Terminal Engine Dashboard",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)
header.pack(pady=10)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

calc_tab = tk.Frame(notebook, bg="#2d2d2d")
server_tab = tk.Frame(notebook, bg="#2d2d2d")
client_tab = tk.Frame(notebook, bg="#2d2d2d")

notebook.add(calc_tab, text="Calculator")
notebook.add(server_tab, text="Server Monitor")
notebook.add(client_tab, text="Client Monitor")

# ============= CALCULATOR FEATURES =============
# Display entry
calc_entry = tk.Entry(calc_tab, font=("Arial", 24), justify='right', bg="#3d3d3d", fg="white")
calc_entry.pack(pady=20, padx=20, fill="x")

# Result display
result_var = tk.StringVar()
result_label = tk.Label(calc_tab, textvariable=result_var, font=("Arial", 18, "bold"), 
                        bg="#2d2d2d", fg="#4CAF50")
result_label.pack(pady=5)

# Button frame
button_frame = tk.Frame(calc_tab, bg="#2d2d2d")
button_frame.pack(pady=10, padx=20)

# Button styling
button_style = {
    "font": ("Arial", 16),
    "bg": "#3d3d3d",
    "fg": "white",
    "width": 5,
    "height": 2
}

operator_style = {
    "font": ("Arial", 16, "bold"),
    "bg": "#FF9800",
    "fg": "white",
    "width": 5,
    "height": 2
}

clear_style = {
    "font": ("Arial", 16, "bold"),
    "bg": "#f44336",
    "fg": "white",
    "width": 5,
    "height": 2
}

def button_click(value):
    current = calc_entry.get()
    calc_entry.delete(0, tk.END)
    calc_entry.insert(0, current + str(value))

def clear_entry():
    calc_entry.delete(0, tk.END)
    result_var.set("")

def calculate():
    try:
        expression = calc_entry.get()
        # Replace ^ with ** for exponentiation
        expression = expression.replace('^', '**')
        # Evaluate the expression
        result = eval(expression)
        # Format result (remove .0 if integer)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        result_var.set(f"= {result}")
    except ZeroDivisionError:
        result_var.set("Error: Division by zero")
    except Exception:
        result_var.set("Error: Invalid expression")

def clear_last():
    current = calc_entry.get()
    calc_entry.delete(0, tk.END)
    calc_entry.insert(0, current[:-1])

def square_root():
    try:
        current = float(calc_entry.get())
        result = math.sqrt(current)
        result_var.set(f"√{current} = {result}")
        calc_entry.delete(0, tk.END)
        calc_entry.insert(0, str(result))
    except:
        result_var.set("Error: Invalid input")

def power_two():
    try:
        current = float(calc_entry.get())
        result = current ** 2
        result_var.set(f"{current}² = {result}")
        calc_entry.delete(0, tk.END)
        calc_entry.insert(0, str(result))
    except:
        result_var.set("Error: Invalid input")

# Row 1: 7 8 9 /
buttons_row1 = [
    ('7', button_click), ('8', button_click), ('9', button_click), ('/', button_click)
]

# Row 2: 4 5 6 *
buttons_row2 = [
    ('4', button_click), ('5', button_click), ('6', button_click), ('*', button_click)
]

# Row 3: 1 2 3 -
buttons_row3 = [
    ('1', button_click), ('2', button_click), ('3', button_click), ('-', button_click)
]

# Row 4: 0 . + =
buttons_row4 = [
    ('0', button_click), ('.', button_click), ('+', button_click), ('=', calculate)
]

# Create buttons for row 1
for i, (text, command) in enumerate(buttons_row1):
    if text in ['/', '*', '-', '+']:
        btn = tk.Button(button_frame, text=text, command=lambda t=text: command(t), **operator_style)
    else:
        btn = tk.Button(button_frame, text=text, command=lambda t=text: command(t), **button_style)
    btn.grid(row=0, column=i, padx=5, pady=5)

# Create buttons for row 2
for i, (text, command) in enumerate(buttons_row2):
    if text in ['/', '*', '-', '+']:
        btn = tk.Button(button_frame, text=text, command=lambda t=text: command(t), **operator_style)
    else:
        btn = tk.Button(button_frame, text=text, command=lambda t=text: command(t), **button_style)
    btn.grid(row=1, column=i, padx=5, pady=5)

# Create buttons for row 3
for i, (text, command) in enumerate(buttons_row3):
    if text in ['/', '*', '-', '+']:
        btn = tk.Button(button_frame, text=text, command=lambda t=text: command(t), **operator_style)
    else:
        btn = tk.Button(button_frame, text=text, command=lambda t=text: command(t), **button_style)
    btn.grid(row=2, column=i, padx=5, pady=5)

# Create buttons for row 4
for i, (text, command) in enumerate(buttons_row4):
    if text == '=':
        btn = tk.Button(button_frame, text=text, command=command, bg="#4CAF50", fg="white", 
                       font=("Arial", 16, "bold"), width=5, height=2)
    elif text in ['/', '*', '-', '+']:
        btn = tk.Button(button_frame, text=text, command=lambda t=text: command(t), **operator_style)
    else:
        btn = tk.Button(button_frame, text=text, command=lambda t=text: command(t), **button_style)
    btn.grid(row=3, column=i, padx=5, pady=5)

# Additional function buttons frame
func_frame = tk.Frame(calc_tab, bg="#2d2d2d")
func_frame.pack(pady=10)

# Clear (C) button
clear_btn = tk.Button(func_frame, text="C", command=clear_entry, **clear_style)
clear_btn.grid(row=0, column=0, padx=5, pady=5)

# Clear last (←) button
clear_last_btn = tk.Button(func_frame, text="←", command=clear_last, **operator_style)
clear_last_btn.grid(row=0, column=1, padx=5, pady=5)

# Square root (√) button
sqrt_btn = tk.Button(func_frame, text="√", command=square_root, **operator_style)
sqrt_btn.grid(row=0, column=2, padx=5, pady=5)

# Power 2 (x²) button
power_btn = tk.Button(func_frame, text="x²", command=power_two, **operator_style)
power_btn.grid(row=0, column=3, padx=5, pady=5)

# ============= SERVER MONITOR =============
server_log = ScrolledText(server_tab, height=25, bg="#1e1e1e", fg="white")
server_log.pack(fill="both", expand=True, padx=10, pady=10)
server_log.insert(tk.END, """Server Connected...
Listening on port 8080
""")

# ============= CLIENT MONITOR =============
client_log = ScrolledText(client_tab, height=25, bg="#1e1e1e", fg="white")
client_log.pack(fill="both", expand=True, padx=10, pady=10)
client_log.insert(tk.END, """Client Connected...
Receiving messages
""")

# ============= SHUTDOWN BUTTON =============
close_btn = tk.Button(root, text="Shutdown Engine", font=("Arial", 14), 
                     bg="#f44336", fg="white", command=root.destroy)
close_btn.pack(pady=15)

root.mainloop()
