#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./LongestCommonPrefix.py

class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res



strs = ["flower","flow","flight"]

s = Solution()
prefix = s.longestCommonPrefix(strs)
print(f'The longest common prefix is: {prefix}')
