import csv
import os
from datetime import datetime
# Operating System
# CSV File
# importing current date and time 2320520037 Debs2705
def save_data(name, weight, height, bmi, category):
    file_exists = os.path.exists("bmi_data.csv")
    write_header = not file_exists or os.stat("bmi_data.csv").st_size == 0
# it will save all the data as a history of records with proper date and time
    with open("bmi_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        
        if write_header:
            writer.writerow(["Name", "Weight", "Height", "BMI", "Category", "Date"])
        
        writer.writerow([name, weight, height, round(bmi, 2), category, datetime.now().strftime("%Y-%m-%d")])
# thank you users for using my application
# hope u enjoyed