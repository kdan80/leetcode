#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./LongestCommonPrefix.py


#------------------------------------------------------------------------------#
#                                                                              #
#  Remove duplicates, in place, from an array without using additional memory  #
#                                                                              #
#------------------------------------------------------------------------------#

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lp = 1

        if len(nums) == 0:
            return 0

        # We use 2 pointers, a right pointer to loop through each integer in the array and a left pointer to pause on each unique value
        # Both pointers initialised to 1
        for rp in range(1, len(nums)):
            # Check each number against the preceding value, if they are not the same we have a new unique value
            if nums[rp] != nums[rp - 1]:
                # Move the new unique number to the position of the left pointer, ie sort it, and then increment the left pointer and continue
                nums[lp] = nums[rp]
                lp += 1
        return lp


s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
res = s.removeDuplicates(nums)
print(f'{res} is the number of unique int in {nums}')
