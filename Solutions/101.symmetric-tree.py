#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True
        
        if root1 == None or root2 == None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
    
    
    

        
# @lc code=end

