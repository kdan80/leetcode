#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./Two_Sum.py


#------------------------------------------------------------------#
#                                                                  #
#  Given an array of integers & an int target, return the indices  #
#  of the two integers that add up to target                       #
#                                                                  #
#------------------------------------------------------------------#


class Solution:
    def twoSum(self, nums, target):

        # val : index
        prevMap = {}

        # Get the index and val of each int in nums
        for i, n in enumerate(nums):
            # If the target - current value is equal to a number that already exists in the array then, then that number and the current number must equal target, so we return a new array with their indices
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i




nums = [2,7,11,15]
target = 17

s = Solution()
res = s.twoSum(nums, target)

print(f'The answer is {res}')
