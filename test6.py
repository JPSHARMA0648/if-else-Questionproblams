#Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and performs the specified operation. Print the result based on the operation.
#ans
# Get input from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operator."

# Print the result
print("Result:", result)
