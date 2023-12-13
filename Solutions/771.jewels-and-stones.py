#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0

        for jew in jewels:
            for stone in stones:
                if jew == stone:
                    result += 1

        
        return result
        
# @lc code=end

