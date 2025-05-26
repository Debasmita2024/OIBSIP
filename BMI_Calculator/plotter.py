import matplotlib.pyplot as plt
import csv
import os
from tkinter import messagebox
# Debasmita Sahu...these are the operating system, csv is the file and matplot is for the graph which will be plotted. 
# Designed by Debasmita Sahu BCA garduate
DATA_FILE = 'bmi_data.csv'

# Define colors for BMI categories
CATEGORY_COLORS = {
    'Underweight': '#ADD8E6',  # light blue
    'Normal': '#C7F9CC',       # light green
    'Overweight': '#FFF3B0',   # light yellow
    'Obese': '#FFCCD5'         # light red
}
# Debasmita Sahu have specified different colours to show you distiction clearly. 
def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'
# this classification will only for the normal, under, obese and over weight. 
# This will not be according to the the logic classification.
def get_bmi_color(bmi):
    if bmi < 18.5:
        return 'blue'
    elif 18.5 <= bmi < 25:
        return 'green'
    elif 25 <= bmi < 30:
        return 'orange'
    else:
        return 'red'

def show_graph():
    if not os.path.isfile(DATA_FILE):
        messagebox.showerror("Error", "No data file found.")
        return

    names = []
    bmis = []

    with open(DATA_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append(row['Name'])
            bmis.append(float(row['BMI']))

    plt.figure(figsize=(12, 6))
# Debasmita created application in such a way that a plot graph will be plotted to help you out more clearly.
    # Filled BMI category regions by Debasmita Sahu design...
    plt.axhspan(0, 18.5, facecolor=CATEGORY_COLORS['Underweight'], alpha=0.5, label='Underweight')
    plt.axhspan(18.5, 25, facecolor=CATEGORY_COLORS['Normal'], alpha=0.5, label='Normal')
    plt.axhspan(25, 30, facecolor=CATEGORY_COLORS['Overweight'], alpha=0.5, label='Overweight')
    plt.axhspan(30, 50, facecolor=CATEGORY_COLORS['Obese'], alpha=0.5, label='Obese')

    # Ploting trend line in graph designed by Debasmita Sahu
    plt.plot(names, bmis, marker='o', color='slateblue', linewidth=2, zorder=3)

    # Adding individual points with category colors to specify and clarify properly 2320520037
    for i, (name, bmi) in enumerate(zip(names, bmis)):
        color = get_bmi_color(bmi)
        plt.scatter(i, bmi, color=color, edgecolor='black', s=100, zorder=5)
        plt.text(i, bmi + 0.3, f"{bmi:.1f}", ha='center', fontsize=10, fontweight='bold', color='black')

    # Threshold lines are also designed by Debs2705
    plt.axhline(18.5, color='blue', linestyle='--', linewidth=1)
    plt.axhline(25, color='orange', linestyle='--', linewidth=1)
    plt.axhline(30, color='red', linestyle='--', linewidth=1)

    # Titles and labels and mentioned and clarified 
    plt.title("BMI Trend", fontsize=18, fontweight='bold', color='#2F4F4F')
    plt.xlabel("Name", fontsize=14, fontweight='bold')
    plt.ylabel("BMI", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Adding legend 2320520037
    plt.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    
    # it will save the figure also as a history of records...
    plt.savefig("bmi_trend_plot.png", dpi=300)

    plt.show()
