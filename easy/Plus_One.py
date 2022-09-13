#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./Plus_One.py


#---------------------------------------------------------------------------------#
#                                                                                 #
#  Given an array of integers add 1 to the last index and carry over if required  #
#                                                                                 #
#---------------------------------------------------------------------------------#


def plusOne(digits):

    # Loop backwards through the array and add 1 to each value
    for i in range(len(digits) - 1, -1, -1):
        x = digits[i] + 1

        # If the additon results in a value of 10 carry over the one
        # If we are at index 0 we cannot carry over the one so we prepend the array with [1]
        if x == 10:
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
            continue
        else:
            digits[i] = x
            break

    return digits

