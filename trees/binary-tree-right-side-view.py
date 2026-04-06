# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for each level, perform a bfs till you arrive at the rightmost node
        # append the val (node.val) of the rightmost node to the output array
        if not root:
            return []

        ans = []

        queue = deque([root])

        while queue:
            # level = []
            curr_level_size = len(queue)

            for i in range(curr_level_size):
                node = queue.popleft()
                # level.append(node.val)
                if i == curr_level_size - 1:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # ans.append(level[-1])

        return ans

        













                