#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict = {char : s.count(char) for char in s}
                        
        for char in t:
            if char not in s or dict[char] == 0:
                return False
            
            dict[char] -= 1
        
        return True
            

                
            
    
         

        
# @lc code=end

