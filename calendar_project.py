import calendar
month = int(input("Enter the month number: "))
year = int(input("Enter the year: "))
if month <1 or month >12:
    print("Invalid month number")
else:
    print(calendar.month(year, month))      