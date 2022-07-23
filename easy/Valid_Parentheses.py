#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./LongestCommonPrefix.py


#---------------------------------------------------------#
#                                                         #
#  Check if parentheses in a string are paired correctly  #
#                                                         #
#---------------------------------------------------------#

class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"}

        for c in s:
            # If c is in c2o then it is a closing parenthesis
            if c in closeToOpen:
                # So we check to see if matches the item on the top of the stack
                if stack and stack[-1] == closeToOpen[c]:
                    # If they match remove from the top stack item
                    stack.pop()
                else:
                    # If they don't match we have an invalid string
                    return False
            # If c is not in c2o then it is an opening parenthesis and should be added to the stack
            else:
                stack.append(c)

        # If we were able to pop all items from the stack we have a valid string
        return True if not stack else False

s = Solution()
str = "()]{}"
res = s.isValid(str)
print(f'{str} is valid = {res}')


