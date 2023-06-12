'''
e.g. 
input
weight = 80
height = 1.75
output
85 / 1.75 * 1.75 = 27.755102040816325
print
your BMI is 28, you are slightly overweight.
'''

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

metric_weight = weight * 0.45359237
metric_height = height / 3.28

bmi = round(metric_weight / metric_height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f}, you are at the normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f}, you are obese.")
else:
    print(f"your BMI is {bmi:.2f}, you are clinically obese.")
