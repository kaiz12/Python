# Write a program that utilizes the concept of conditional execution, takes a string as input, and:

# - prints the sentence "Yes - Spathiphyllum is the best plant ever!"
#   to the screen if the inputted string is "Spathiphyllum" (upper-case)

# - prints "No, I want a big Spathiphyllum!"
#   if the inputted string is "spathiphyllum" (lower-case)

# - prints "Spathiphyllum! Not [input]!" otherwise.
#   Note: [input] is the string taken as input.



word = input("Please enter the word here ->")
if word == "SPATHIPHYLLUM":
    print("Yes - Spathiphyllum is the best plant ever!")
elif word == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not [input]!")