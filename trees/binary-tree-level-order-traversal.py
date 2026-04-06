from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        ans = []


        # for each level add all the vals to current_level: List[int]
        # then add current_level to ans



        # use a deque
        queue = deque([root])

        while queue:
            current_level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()  # remove from the front
                current_level.append(node.val)

                # and new right and left elements for the curr node(starting from left to right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add the vals of the curr level to the final result
            ans.append(current_level)

        return ans


        
