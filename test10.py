'''Q10 Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in
kilograms) and height (in meters). Then categorize the BMI into:
Underweight (BMI < 18.5)
Normal weight (18.5 <= BMI < 24.9)
Overweight (25 <= BMI < 29.9)
Obesity (BMI >= 30)
Use the formula: BMI = weight / (height ** 2)'''

#ans
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Categorize BMI
category = categorize_bmi(bmi)

# Output the result
print(f"Your BMI is: {bmi:.2f}")
print(f"Your BMI category is: {category}")
