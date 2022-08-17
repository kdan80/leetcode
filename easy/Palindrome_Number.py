#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./Palindrome_Number.py


#----------------------------------------------------------------#
#                                                                #
#  Given an integer x, return true if x is a palindrome integer  #
#                                                                #
#----------------------------------------------------------------#


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # If x is less than zero, ie negative, it cannot be a palindrome
        if x < 0: return False

        # We will use this divider to grab the first digit of x, eg for 1223 the first digit is 1, for 223 the first digit is 2
        # Later we will compare the first digit to the last digit
        div = 1

        # In order for the divider to grab the first digit it has to be of the same order of magnitude eg for 1223 div must be 1000, for 223 it must be 100
        # Thus 1223 // 1000 will give us 1, ie the first digit
        # And 1223 % 10 will give us 3, ie the last digit
        while x > 10 * div:
          div *= 10

        # Now we can compare the first digit (x // div = 1) to the last digit (x % 10 = 3) if they are equal we reduce x by a factor of 10 and div by a factor of 10*2 and continue the loop
        # If they are not equal then we do not have a palidrome and can immediately return
        while x:
          if x // div != x % 10: return False

          x = (x % div) // 10
          div = div / 100
        return True

s = Solution()

isPalindrome = s.isPalindrome(1221)

print(f'122 is a palindrome = {isPalindrome}')
