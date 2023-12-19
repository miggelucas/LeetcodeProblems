#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen = set()

        for number in nums:
            if number in seen:
                seen.remove(number)
            else:
                seen.add(number)

        return seen.pop()
        
        
# @lc code=end

