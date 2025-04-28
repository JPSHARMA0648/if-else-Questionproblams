'''Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
triangle. A triangle is valid if the sum of any two sides is greater than the third side.
Check conditions like a + b > c, b + c > a, and a + c > b.'''

#ans
# Get the three sides from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check the triangle inequality conditions
if (a + b > c) and (b + c > a) and (a + c > b):
    print("The sides form a valid triangle.")
else:
    print("The sides do NOT form a valid triangle.")
