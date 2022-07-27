#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./LongestCommonPrefix.py


#------------------------------------------------------------------------#
#                                                                        #
#  Return the index of the first occurrence of str1 in str2 or -1 if it  #
#  does not appear                                                       #
#                                                                        #
#------------------------------------------------------------------------#


class Solution:
    def strStr(self, haystack, needle):

        # This is included as per leetcode instructions but this check is illogical and should really return -1
        if needle == "":
            return 0

        # If haystack is shorter than needle then needle can not be in haystack, ie hello can not be in ello
        if len(haystack) < len(needle):
            return -1

        # Loop through haystack and look for the first letter of needle
        # If we find it start a second loop and check for the remaining letters
        # If loop2 is successful then needle is in haystack so we return i
        # If the loop2 is unsuccessful we break out and continue loop1
        # If both loops were unsuccessful needle is not in haystack and we return -1
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                    if j == len(needle) - 1
                        return i

        return -1

s = Solution()
res = s.strStr('hello', 'll')
print(res)
