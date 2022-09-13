#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./14.LongestCommonPrefix.py


#---------------------------------------------------------#
#                                                         #
#  Find the longest common prefix in an array of strings  #
#                                                         #
#---------------------------------------------------------#


class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""

        # Create a loop based on string length, ideally this would be the shortest string in the array but if not we can do an out of bounds check later
        for i in range(len(strs[0])):
            # For each string, check if it is longer than the above range, if it is we are out of bounds
            # We also check if the char at position s[i] is the same as the first string's char at s[i]'
            # If both checks pass then all strings have the char at position s[i] in common and we add it to the prefix and continue the loop
            # If either of the checks fail we have found the end of the longest common prefix and should return
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res



strs = ["flower","flow","flight"]

s = Solution()
prefix = s.longestCommonPrefix(strs)
print(f'The longest common prefix is: {prefix}')
