import pyperclip
from tkinter import messagebox
from datetime import datetime
# it will import the date and time 
# Debasmita application imported libraries and framworks which are needed
def copy_to_clipboard(password):
    if password and not password.startswith("Error"):
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No valid password to copy.")
# password export hone ke liye ye code use hoga 
def export_password(password):
    with open("saved_passwords.txt", "a") as f:
        f.write(f"{datetime.now()} — {password}\n")
    messagebox.showinfo("Exported", "Password saved to file.")
# thank you for using my Security Tool