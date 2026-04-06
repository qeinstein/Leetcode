# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True   # It's a subtree if it's empty
        if not root: return False  # if s is empty and t is not return False

        if self.sameTree(root, subRoot):
            return True

        # now if they're not same
        return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))



    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:   # THis is needed to check if the trees equal
        if not s and not t: # if thye are both empty they are equal
            return True
        
        if s and t and s.val == t.val:
            return (self.sameTree(s.right, t.right) and self.sameTree(s.left, t.left))

        return False