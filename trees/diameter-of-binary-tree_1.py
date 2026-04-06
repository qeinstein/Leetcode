# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diameter = 0
        
        def get_height(node):
            if not node:
                return -1 # Use -1 if diameter is edges, 0 if diameter is nodes
            
            # Recursively find the height of left and right subtrees
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            
            # The diameter at the current node
            current_diameter = left_h + right_h + 2
            
            # Update the global maximum diameter found so far
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the height of this node to the parent
            return 1 + max(left_h, right_h)
        
        get_height(root)
        return self.max_diameter