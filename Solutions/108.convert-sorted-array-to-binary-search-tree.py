#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        middleIndex = len(nums) // 2
        return TreeNode(val= nums[middleIndex],
                        left= self.sortedArrayToBST(nums[ : middleIndex]),
                        right= self.sortedArrayToBST(nums[middleIndex + 1 : ]))
        

        
  
   
# @lc code=end

