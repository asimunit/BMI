import unittest
from task import *




def Body_Mass_Index_test():
    
    data_arr = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
            85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
            "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
            "HeightCm": 167, "WeightKg": 82}]
    result = Add_column(data_arr)
    check = [{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'Body_Mass_Index': 32.83}, {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85, 'Body_Mass_Index': 32.79}, {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'Body_Mass_Index': 23.77}, {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'Body_Mass_Index': 22.5}, {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70, 'Body_Mass_Index': 31.11}, {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82, 'Body_Mass_Index': 29.4}]
    if result == check:
        return "Body_Mass_Index Test case passed"
    else:
        return "Body_Mass_Index test case failed"
    
def total_number_of_overweight_test():
    
    data_arr = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
            85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
            "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
            "HeightCm": 167, "WeightKg": 82}]
    result = total_number_of_overweight(data_arr)
    check = 0
    if result == check:
        return "total_number_of_overweight_test Test case passed"
    else:
        return "total_number_of_overweight_test test case failed"

if __name__ == '__main__':
    print(Body_Mass_Index_test())
    print(total_number_of_overweight_test())

  