"""Q12 Write a program that takes the name of a month as input and prints the number of days in that
month. Consider leap years for February."""
#ans
def days_in_month(month, year):
    # Dictionary with the number of days in each month
    months_with_days = {
        "January": 31,
        "February": 28,  # Default days for February
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    # Check for leap year and adjust February's days
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        months_with_days["February"] = 29

    return months_with_days.get(month, "Invalid month")

# Get user input
month = input("Enter the name of the month: ")
year = int(input("Enter the year: "))

# Get the number of days in the month
days = days_in_month(month, year)

# Output the result
if isinstance(days, int):
    print(f"The number of days in {month} {year} is: {days}")
else:
    print(days)
