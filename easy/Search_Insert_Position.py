#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./Search_Insert_Position.py


#------------------------------------------------------------------#
#                                                                  #
#  Given a sorted array of distinct integers and a target value,   #
#  return the index if the target is found. If not, return the     #
#  index where it would be if it were inserted in order.           #
#                                                                  #
#------------------------------------------------------------------#


class Solution:
    def searchInsert(self, nums, target):

        # Initialise 2 pointers at the start and end of the nums array
        lp, rp = 0, len(nums) - 1

        # Find the midpoint between the 2 pointers
        while lp <= rp:
            mid = (lp + rp) // 2

            # Look at the value at the mid point, if it is equal to the target we have found it and should return the index of the mid point
            if target == nums[mid]:
                return mid

            # If the target is greater than the midpoint value we need to shift right and continue the loop otherwise we need to shift left and continue
            if target > nums[mid]:
                lp = mid + 1
            else:
                rp = mid - 1

        return lp
