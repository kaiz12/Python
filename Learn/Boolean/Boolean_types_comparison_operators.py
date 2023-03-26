# Program reacts according to the recived answers
# Computers know two types of answers Yes, this is true and No, this is false
# To ask questions Python uses operators

# Q: is two values equal
# A: use the == (equal operator) , remember = is assignment
# a == b compares a and b
# it is a binary operator with left-sided binding. It needs two arguments to check if they are equal.

print(2 == 2)  # Is True
print(2 == 2.)  # Because Python is able to convert integer value to its real equivalent - it's True
print(1 == 2)  # This is False

#EQUALITY
# == (equal)operator

#var == 0
# We cannot find the answer if we don't know what value is stored in the variable var
var = 0
print(var == 0)
var = 1
print(var == 0)

# != (not equal)operator
#
# It compares the two operands,
# if they are equal the result is False,
# if they are not equal the result is True

var = 0 # Assigning 0 to var
print(var !=0)

var = 1 # Assigning 1 to var
print(var !=0)

# GREATER THAN (OR EQUAL)


# > (greater than) operator

# If you want to know is there more black sheep than white ones
# black_sheep > white_sheep
# True confims it; False denies it.


# >= (greater than or equal) operator

# It's a non-strict variant of > (greater than)

# Both of these operators (strict an non-strict) as two others < and <= are
# binary operators with left-sided binding,
# and their priority is greater than shown by == and != (equal and not equal)

# centigrade_outside >= 0.0 #Greater than or equal to


# <= (less than or equal to) operator

# It's opposite of greater than greater than or equal

# current_velocity_mph < 85 # Less than
# current_velocity_mph <= 85 # Less than or equal to

# To use the answer of comparison you can store it in a variable
# answer = number_of_lions >= number_of_lionesses

###
# PIORITY TABLE
#
# Priority   Operator
# 1          +,-         unary
# 2          **
# 3          *,/,//,%
# 4          +,-         binary
# 5          <,<=,>,>=
# 6          ==,!=
###