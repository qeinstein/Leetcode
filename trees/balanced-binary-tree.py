# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode])-> int:
            if node is None:
                return 0

            return 1 + max(height(node.left), height(node.right))


        if root is None:
            return True

        # Get the height of left and right sub trees
        lHeight = height(root.left)
        rHeight = height(root.right)

        if abs(lHeight - rHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
            