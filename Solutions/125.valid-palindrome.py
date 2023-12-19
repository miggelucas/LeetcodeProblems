#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""

        for char in s:
            if char.isalnum():
                newString += char.lower()

    
        return newString == newString[::-1]
        


        
# @lc code=end

