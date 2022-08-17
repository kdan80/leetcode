#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./Remove_Element.py


#------------------------------------------------------------------------------#
#                                                                              #
#  Remove instances of val in an array, nums, without using additional memory  #
#                                                                              #
#------------------------------------------------------------------------------#


class Solution:
    def removeElement(self, nums, val):

        # This is simple for, as long as val is in nums == true remove val from nums
        while(val in nums):
            nums.remove(val)
        return len(nums)

s = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
k = s.removeElement(nums, 5)
print(nums)
print(k)
