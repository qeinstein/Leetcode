class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None # Use a class variable to store the result when found

        def dfs_descendant(node: 'TreeNode') -> bool:
            if not node:
                return False

            # to check if th curr node is p or q
            mid = (node.val == p.val or node.val == q.val)

            # recursively check left and right subtrees
            left = dfs_descendant(node.left)
            right = dfs_descendant(node.right)

            # if any two of these are True (mid, left, or right), 
            # this node is the Lca
            if (mid + left + right) >= 2:
                self.ans = node

            # return True if this node or any of its descendants is p or q
            return mid or left or right

        dfs_descendant(root)
        return self.ans