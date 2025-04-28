#Write a program that takes a percentage (integer) as input and prints the corresponding grade based
on the following criteria:
>= 90: Grade A
>= 80: Grade B
>= 70: Grade C
>= 60: Grade D
< 60: Grade F

#ans.
# Get percentage input from the user
percentage = int(input("Enter your percentage: "))

# Determine the grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

# Print the grade
print(f"Your grade is: {grade}")
