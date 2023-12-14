#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        number = 1

        while number * number <= x:
            number += 1

        return number - 1
        
        
# @lc code=end

