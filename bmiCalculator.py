height = input("Enter your height in lbs: ")
weight = input("Enter your weight in feet: ")

w = float(weight) * 0.45359237
h = float(height) / 3.28

bmi = (w / h**2)

print(int(bmi))
