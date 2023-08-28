import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return
        
        result_label.config(text=f"Result: {result}")
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and configure widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry_num1 = tk.Entry(frame)
entry_num1.pack(side=tk.LEFT)

operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(frame, operation_var, *operation_choices)
operation_var.set("+")
operation_menu.pack(side=tk.LEFT)

entry_num2 = tk.Entry(frame)
entry_num2.pack(side=tk.LEFT)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
