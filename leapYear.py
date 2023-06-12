'''
e.g. The year 200:
2000 /4 = 500(leap)
2000 /100 = 20(not leap)
2000/400 = 5(leap!)
So The leap year 2000 is a leap year
'''
year = (int(input("Which year do want to check? ")))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")
