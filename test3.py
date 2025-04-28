#Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100unless it is also divisible by 400.# Get the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
