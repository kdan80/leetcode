#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./58.Length_Of_Last_word.py


#--------------------------------------------------#
#                                                  #
#  Return the length of the last word in a string  #
#                                                  #
#--------------------------------------------------#


class Solution:
    def lengthOfLastWord(self, s):

        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length


s = Solution()

print(s.lengthOfLastWord("Hello World  "))
