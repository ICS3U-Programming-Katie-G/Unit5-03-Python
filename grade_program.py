#!/usr/bin/env python3
# Created by: Katie G
# Created on: December 19th, 2022
# This program will get the user's level as a string in main(),
# then it will pass it to the calc_mark() function, where, using an
# if... else if... else statement, the program will set the
# middle percentage of the level, then using a return statement,
# the middle percentage is passed back to the main() function,
# where it will be displayed back to the user.


# this function will check to see which middle percentage the user's
# inputted level corresponds with! It then returns the result back
# to main() to be displayed.
def calc_marc(level):
    # defining the variable for the middle percentage.
    middle_percent = 0

    # checking to see which middle percentage the user's level corresponds to,
    # using an if... else if... else statement.
    if level == "4++":
        middle_percent = 100
    elif level == "4+":
        middle_percent = 97
    elif level == "4":
        middle_percent = 90
    elif level == "4-":
        middle_percent = 83
    elif level == "3+":
        middle_percent = 78
    elif level == "3":
        middle_percent = 74
    elif level == "3-":
        middle_percent = 71
    elif level == "2+":
        middle_percent = 68
    elif level == "2":
        middle_percent = 64
    elif level == "2-":
        middle_percent = 61
    elif level == "1+":
        middle_percent = 58
    elif level == "1":
        middle_percent = 54
    elif level == "1-":
        middle_percent = 51
    elif level.upper() == "R":
        middle_percent = 25
    # this condition is for if the user inputs a valid string, but it
    # is not one of the accepted levels.
    else:
        middle_percent = -1

    # this will return the middle percentage back to main()
    return middle_percent


# this function will get the user level as a string, then pass it onto
# the next function. It will also receive the middle percentage and
# display it back to the user.
def main():
    # getting the user input
    user_level = input("Hello! Please insert your mark as a level! ")

    # passing the user mark onto the calc_marc() function, and setting the return
    # value to this variable.
    calculated_middle = calc_marc(user_level)

    # printing the calculated middle percentage mark.
    print(
        "Your mark level of {} is equivalent to the middle percentage mark of {}%".format(
            user_level, calculated_middle
        )
    )


if __name__ == "__main__":
    main()
