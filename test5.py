#Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.

#ans.
# Get a single character input from the user
letter = input("Enter a single letter: ").lower()

# Check if it's a letter and has only one character
if len(letter) == 1 and letter.isalpha():
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("Please enter a single alphabet letter.")
