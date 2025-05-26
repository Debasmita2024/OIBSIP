# logic.py
# Logic is created by Debasmita Sahu very simple and easy BMI CALCULATOR
def calculate_bmi(weight, height):
    return weight / (height ** 2)
# I, Debasmita Sahu kept this classification to make it more specific and know your exact state of body condition as per your BMI.
def classify_bmi(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif bmi < 17:
        return "Moderate Thinness"
    elif bmi < 18.5:
        return "Mild Thinness"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class I"
    elif bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"
# If you are in normal range, then fine.....Debasmita Sahu 2320520037 KL University HYD BCA 2nd year
# If you are obese then decrease ur weight or else it will be hazardous for you. 
# Debs2705 My code