#! /usr/bin/env python3

# This file will need to have the execute permission set
# chmod +x ./Roman_to_Integer.py


#-----------------------------------------#
#                                         #
#  Convert a Roman numeral to an integer  #
#                                         #
#-----------------------------------------#


class Solution:
    def romanToInt(self, s):
        roman = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }

        res = 0

        for i in range(len(s)):
            # Loop through each roman numeral if the current value is less than the value next to it we have a subtractive numeral, eg IV, so we subtract it from the result, otherwise we add it
            # We also need to check we are still in bounds with i + 1 < len(s)
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        return res


s = Solution()
roman = 'CMXCVIII'
res = s.romanToInt(roman)
print(f'{roman} = {res}')
