#Write a program that takes three numbers as input and prints the largest of the three.

# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
largest = max(num1, num2, num3)

# Print the result
print(f"The largest number is: {largest}")
