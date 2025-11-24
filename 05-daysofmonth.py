month = int(input("Enter month number (1-12): "))

months = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

if month == 2:
    leap = input("Leap year? (yes/no): ")
    if leap.lower() == "yes":
        print("29 days")
    else:
        print("28 days")
elif month in months:
    print(months[month], "days")
else:
    print("Not a real month")