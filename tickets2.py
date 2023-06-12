height = float(input("What is your height?"))
age = int(input("what is your age?"))
bill = 0

if height >= float(5.4):
    print("You can ride the rollercoaster!")
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo_option = input("Do you want a photo take? Y or N. ")
    if photo_option == "Y" or photo_option == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have not grow taller before you can ride.")
# video 33
