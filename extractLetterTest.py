def FindDaysandMonths():
    dateString = input("Enter a date (MMDD): ")

    startDays = 2
    startMonths = 0
    days = dateString[startDays:startDays+2]
    months = dateString[startMonths:startMonths+2]

    print("The month is", months, "and the day of the month is", days)

FindDaysandMonths()