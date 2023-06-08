print("Welcome to the tip calculator.")

total = input("What was the total bill? ")
percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

per_num = (float(percentage) / 100) + 1
results = (float(total) * float(per_num)) / int(people)
print(f"Each person should pay: ${results:.2f}")
