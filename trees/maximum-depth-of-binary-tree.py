# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # first approach below (recursion, beats 100%)
        # if not root:
        #     return 0

        # height = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # return height

        # second approach
        depth = 0
        if not root:
            return 0

        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth
