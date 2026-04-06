# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs 
        # for left subtree everything belpw is strictly smaller, opp for the right 

        def dfs(node: Optional[TreeNode], low = -float('inf') , high = float('inf')):
            # check if root is none
            if not node:
                return True # An empty node is a valid bts

            if not (low < node.val < high):
                return False    # Curr node has to be btw low and high            
            # if node.left:
            #     if node.left.val >= node.val:
            #         return False
                
            # if node.right:
            #     if node.right.val <= node.val:
            #         return False

            # dfs(node.left)
            # dfs(node.right)

            # recursively check left and right subtree
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root)

