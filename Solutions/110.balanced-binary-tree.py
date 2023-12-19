#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        dif = abs(leftHeight - rightHeight)
        
        return dif < 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
      
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        highestBranch = max(self.height(root.left),
                            self.height(root.right))
        return 1 + highestBranch
        
# @lc code=end

