#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        number = int(len(candyType) / 2)

        uniqueCandy = set(candyType)

        if len(uniqueCandy) < number:
            return len(uniqueCandy)
        
        return number
        

        
# @lc code=end

