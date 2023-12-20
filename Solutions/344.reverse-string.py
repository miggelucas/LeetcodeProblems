#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # trying 2 pointers

        bottomIndex = 0
        topIndex = len(s) - 1

        while bottomIndex < topIndex:
            aux = s[bottomIndex]
            s[bottomIndex] = s[topIndex]
            s[topIndex] = aux

            bottomIndex += 1
            topIndex -= 1
        
        
# @lc code=end

