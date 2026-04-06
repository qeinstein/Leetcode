# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for every node in the tree
        # what if i just keep track of the highest so far 
        # how do u even know the path i am on?

        count = 0

        def dfs(node, maxVal):
            nonlocal count
            if not node:
                return

            if node.val >= maxVal:
                count += 1

            newMax = max(maxVal, node.val)
            dfs(node.left, newMax)
            dfs(node.right, newMax)

        dfs(root, root.val)
        return count
