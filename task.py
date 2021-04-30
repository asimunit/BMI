
def BMI(weight,height):
    return weight/( height/100)**2

def BMI_Range(bmi):
    if bmi < 18.4:
        return "Underweight"
    elif bmi > 18.5 and bmi < 24.9:
        return "Normal weight"
    elif bmi > 25 and bmi < 29.9:
        return "Overweight"
    elif bmi > 30 and bmi < 34.9:
        return "Moderately obese"
    elif bmi > 35 and bmi < 39.9:
        return "Severely obese"
    else:
        return "Very severely obese"

def Add_column(data_arr):
    for i in data_arr:
        res = round(BMI(i["WeightKg"],i["HeightCm"]),2)
        i["Body_Mass_Index"] = res
    return data_arr

def total_number_of_overweight(data_arr):
    total_overweight = 0
    for i in data_arr:
        bmi = BMI(i["WeightKg"],i["HeightCm"])
        res = BMI_Range(bmi)
        if res == "Overweight":
            total_overweight += 1
    return total_overweight
