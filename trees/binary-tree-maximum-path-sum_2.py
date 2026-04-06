# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # max path sum
        # path with the maximum sum basically.
        # rn, i know it's a dp based question
        # how to apply dp?, idk yet
        # first thing that comes to mind is checking all posible
        # paths in the tree and update max path sum as i continue

        highest_sum = -float('inf')

        """a helper function that visits a node and returns the max single
        branch sum it can provide to its parent"""
        def helper(node: Optional[TreeNode]) -> int:

            nonlocal highest_sum
            # if curr node is null return 0
            if not node:
                return 0

            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)

            current_path_sum = node.val + left_gain + right_gain

            highest_sum = max(highest_sum, current_path_sum)

            return node.val + max(left_gain, right_gain)


        helper(root)
        return highest_sum