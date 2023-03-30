# Pseudocode is code that has notation which is not an actual programming language
# (it can be neither compiled nor executed), but it is formalized, concise and readable

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02

# Performing certain part of code more than once is called loop.
# Lines 02 through 08 make a loop.
# We'll pass through them as many times as needed to review all the entered values.