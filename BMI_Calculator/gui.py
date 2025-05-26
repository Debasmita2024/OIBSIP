# gui.py
# Debasmita GUI CODE for giving it a frame like name, weight, height.
import tkinter as tk
from tkinter import messagebox
from logic import calculate_bmi, classify_bmi
from storage import save_data
from plotter import show_graph
# these are the libraries and frameworks by Debasmita Sahu 2320520037
def start_app():
    root = tk.Tk()
    root.title("BMI Calculator")

    tk.Label(root, text="Name:").grid(row=0, column=0)
    tk.Label(root, text="Weight (kg):").grid(row=1, column=0)
    tk.Label(root, text="Height (m):").grid(row=2, column=0)
# Debasmita allows you to enter your name, age and calculate the BMI
    entry_name = tk.Entry(root)
    entry_weight = tk.Entry(root)
    entry_height = tk.Entry(root)
# you can see the label of BMI as offered by DEBASMITA SAHU from KL HYD
    entry_name.grid(row=0, column=1)
    entry_weight.grid(row=1, column=1)
    entry_height.grid(row=2, column=1)
# you can also see the graph as offered by DEBASMITA SAHU from KL HYD 
    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    def on_submit():
        try:
            name = entry_name.get()
            weight = float(entry_weight.get())
            height = float(entry_height.get())

            if not name or weight <= 0 or height <= 0:
                raise ValueError
# logic login my logic calculation as per standard rules and regulations
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
            result_label.config(text=f"BMI: {bmi:.2f} ({category})")
            save_data(name, weight, height, bmi, category)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid name, weight, and height.")
# see you are under, normal or over weight as ur your height and weight 
    tk.Button(root, text="Calculate BMI", command=on_submit).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(root, text="View Graph", command=show_graph).grid(row=5, column=0, columnspan=2)

    root.mainloop()
# Thank you for using my application 
# By Debasmita Sahu BCA 2nd year KL University HYD Telangana