# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder traversal
        # visit (left, root, right)

        # Recursive solution
        """
        output = []
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            output.append(root.val)
            dfs(root.right)

        dfs(root)
        return output
        """

        # Iterative Solution
        stack, res = [], []
        curr = root

        while curr or stack:

            # going as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # we can visit it because it doesn't have anymore left children
            curr = stack.pop()
            res.append(curr.val)

            # process the right side of the guy we just did
            curr = curr.right

        return res