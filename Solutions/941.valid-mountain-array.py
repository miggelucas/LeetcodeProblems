#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ascending: bool = True

        if len(arr) < 3:
            return False

        for i in range(0, len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            
            if not ascending:
                if arr[i] < arr[i + 1]:
                    return False
            
            if arr[i] > arr[i + 1]:
                if i < 1:
                    return False
                ascending = False
        
        if ascending == True:
            return False
        
        return True
            
                
            

        
# @lc code=end

