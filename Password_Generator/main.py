import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from modules.generator import generate_password
from modules.utils import copy_to_clipboard, export_password
# Debasmita Sahu imported these libraries and frameworks 
# Doing Window setup for building proper environment for the project
root = tb.Window(themename="minty")
root.title("🔐 Advanced Password Generator")
root.geometry("600x400")
root.resizable(True, True)
root.configure(bg="#f3e8ff")

# Variables which Debs2705 is using to build this project
password_var = tk.StringVar()
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

# Main frame which Debs2705 is making for better visibility and clarity of the application
main_frame = tb.Frame(root, padding=20)
main_frame.pack(pady=10)

# Header of my application will be like this 
tb.Label(main_frame, text="🔐 PASSWORD GENERATOR", font=("Helvetica", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Length and all will be adjusted by my design which I assigned
tb.Label(main_frame, text="🔢 Length:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="e", padx=5)
length_entry = tb.Entry(main_frame, width=10, font=("Helvetica", 12), bootstyle="info", justify="center")
length_entry.insert(0, "12")
length_entry.grid(row=1, column=1, sticky="w", padx=5)

tb.Label(main_frame, text="🚫 Exclude:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
exclude_entry = tb.Entry(main_frame, width=30, font=("Helvetica", 12), bootstyle="info")
exclude_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# 2320520037 BCA student from HYD Telangana
options_frame = tb.LabelFrame(main_frame, text="Character Options", padding=10, bootstyle="secondary")
options_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

tb.Checkbutton(options_frame, text="Include Uppercase (A-Z)", variable=upper_var, bootstyle="success").pack(anchor="w", pady=2)
tb.Checkbutton(options_frame, text="Include Lowercase (a-z)", variable=lower_var, bootstyle="success").pack(anchor="w", pady=2)
tb.Checkbutton(options_frame, text="Include Digits (0-9)", variable=digit_var, bootstyle="success").pack(anchor="w", pady=2)
tb.Checkbutton(options_frame, text="Include Symbols (!@#$)", variable=symbol_var, bootstyle="success").pack(anchor="w", pady=2)

# Generating Function to apply it properly
def generate_and_display():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        password_var.set("Invalid length")
        return
# exception handling 
    password = generate_password(
        length,
        upper_var.get(),
        lower_var.get(),
        digit_var.get(),
        symbol_var.get(),
        exclude_entry.get()
    )
    password_var.set(password)

# Buttons which i will be using in my application
tb.Button(main_frame, text="🎯 Generate Password", bootstyle="primary outline", command=generate_and_display).grid(row=4, column=0, columnspan=2, pady=10)

# Password will be displayed like this as I mentioned here
tb.Entry(main_frame, textvariable=password_var, font=("Courier", 12), width=40, justify="center", bootstyle="secondary").grid(row=5, column=0, columnspan=2, pady=5)

# Debs2705 kept copy and export button
# copy button will help to copy
# expot button will help to save it for future
# you dont need to rememeber your password as it will be saved
action_frame = tb.Frame(main_frame)
action_frame.grid(row=6, column=0, columnspan=2, pady=10)

tb.Button(action_frame, text="📋 Copy", bootstyle="success outline", command=lambda: copy_to_clipboard(password_var.get())).pack(side="left", padx=10)
tb.Button(action_frame, text="💾 Export", bootstyle="info outline", command=lambda: export_password(password_var.get())).pack(side="left", padx=10)

# Footer of Debasmita Security Tools will be displayed like this
tb.Label(root, text="© 2025 Debasmita Security Tools", font=("Helvetica", 9), background="#f3e8ff").pack(pady=(10, 5))
# my application
root.mainloop()
