# We have to have mechanism which will allow you to do something
# If a condition is met, and not do it if it isn't

# To make such decisions we have conditional instruction (or conditional statement)

###
# if true_or_not:
#    do_this_if_true
###

# Conditional statement consists of the following - strictly:
# - the if keyword;
# - one or more whitespaces;
# - an expression (a question or an answer) whose value will be interpreted solely in terms of True
#   (when value is non-zero) and False (when it's equal to zero);
# - a colon followed by a newline;
# - an indented instruction or set of instructions (at least one instruction is absolutely required);
#   the indentation may be achieved by inserting 4 or more spaces or using a tab character.
#   If there is more than one instruction you cant mix spaces and tabs. Python 3 doesn't allow to mix them.

# If true_or_not expression represents the truth (i.e, it's value is not equal to zero),
# the indented statement(s) will be executed;

# If true_or_not expression does not represent the truth (i.e, it's value is equal to zero),
# the indented statement(s) will be omitted (ignored), and the next executed instruction will be the one
# after the original indentation level.

# In real life, we express a desire:
# If the weather is good, we'll go for a walk
# then, we'll have lunch

# Having lunch is not a conditional activity and doesn't depend on the weather

###
# if the_weather_is_good:
#     go_for_a_walk()
# have_lunch()


# IF STATEMENT

# Example 1
if sheep_counter >= 120:    # Evaluate a test expression
    sleep_and_dream()       # Execute if test expression is True

# You can read it as: if sheep_counter is geater than or equal to 120, then fall asleep and dream
# (i.e, execute the sleep_and_dream function)

# Example 2
if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()

# Makeing a bed, taking a shower and falling asleep and dreaming are all executed conditionally
# - when sheep_counter reaches the desired limit

# Feeding the sheepdogs, however, is always done (i.e, the feed_the_sheepdogs() function
# isn't indented and does not belong to the if block, which means it is always executed).


# IF-ELSE STATEMENT

# Example 1
"If the weather is good, we will go for a walk, otherwise we will go to a theater."

# Now we know what we'll do if the conditions are met, and we know what we'll do if not everything goes our way.
# In other words we have plan B.

if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

# There is new word: else - this is a keyword.
# The part of the code which begins with else
# says what to do if the condition specified for the if is not met (not the colon after the word).

# If the condition evaluates to True (its value is not equal to zero),
# the perform_if_condition_true statement is executed, and the conditional statement comes to an end;

# If the conition evaluates to False (it is equal to zero),
# the perform_if_condition_false statement is executed, and the conditional statement comes to an end;

# Example 2 (more conditions)

if the_weather_is_good:
    go_fo_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()
have_launch()

# If the weather is good, we'll go for a walk and have fun. Otherwise, we'll go to a theatre and enjoy the movie.
# No matter if the weather is good or bad, we'll have launch afterwards (after the walk or after going to the theatre).

#Example 3 (nested if-else)

# Consider the case where the instruction placed after the if is another if.

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_launch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

# this use of the if statement is known as nesting; remember that every else refers to the if which lies at the same identation level;
# you need to know this to determine how the ifs and elses pair up;

# consider how the indentation improves readability, and makes the code easier to understand and trace.


# ELIF STATEMENT

# As you probably suspect, it's another form of else if.
# elif is use to check more than one condition, and stop when the first statement which is true is found.

# Example 1

if the_wheater_is_good:
    go_for_a_walk()
elif tickets_are_availale:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

# The way to assemble subsequent if-elif-else statements is sometimes called a cascade.

# - You mustn't use else without a preceding if;
# - else is always the last branch of the cascade, regardless of whether you've used elif or not;
# - else is an optional part of the cascade, and may be omitted;
# - if there is an else branch in the cascade, only one of all the branches is executed;
# - if there is no else branch, it's possible that none of the available branches is executed.
