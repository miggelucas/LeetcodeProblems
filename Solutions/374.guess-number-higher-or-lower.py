#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
            
            bottomIndex = 1
            topIndex = n
    
            while bottomIndex <= topIndex:
                middleIndex = (bottomIndex + topIndex) // 2
    
                guessResult = guess(middleIndex)
    
                if guessResult == 0:
                    return middleIndex
    
                elif guessResult == -1:
                    topIndex = middleIndex - 1
    
                else:
                    bottomIndex = middleIndex + 1
    
            return -1
    
        
# @lc code=end

