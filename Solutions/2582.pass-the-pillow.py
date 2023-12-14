#
# @lc app=leetcode id=2582 lang=python3
#
# [2582] Pass the Pillow
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        index = 1
        ascending = 1

        for i in range(1, time + 1):
            index += 1 * ascending

            if index == n:
                ascending = -1
            elif index == 1:
                ascending = 1
        
        return index

          
               
           


    
        
# @lc code=end

