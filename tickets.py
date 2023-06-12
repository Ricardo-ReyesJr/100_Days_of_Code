height = float(input("What is your height?"))
age = int(input("what is your age?"))

if height >= float(5.4):
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have not grow taller before you can ride.")
