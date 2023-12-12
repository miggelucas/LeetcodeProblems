#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        a = int(a, 2)
        b = int(b, 2)
        # Add the integers
        c = a + b
        # Convert the sum back to a binary string
        c = bin(c)
        # Remove the '0b' prefix
        c = c[2:]
        return c

        

                       
        
# @lc code=end

