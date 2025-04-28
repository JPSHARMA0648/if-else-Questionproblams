'''Q =Write a program that checks if a username and password entered by the user match the pre-set values
username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
"Login Failed".'''
#ans
# Pre-set credentials
correct_username = "admin"
correct_password = "1234"

# Get input from the user
username = input("Enter username: ")
password = input("Enter password: ")

# Check if the entered credentials match
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Login Failed")
