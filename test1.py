#Write a program that takes an integer input from the user and checks whether the number is odd or
even.

# Get input from the user
number = int(input("Enter an integer: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
