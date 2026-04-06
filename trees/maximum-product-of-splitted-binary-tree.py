class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []

        # DFS to calculate sums bottom-up
        def get_sums(node):
            if not node:
                return 0
            
            # The sum of this subtree is:
            # current value + left subtree sum + right subtree sum
            current_sum = node.val + get_sums(node.left) + get_sums(node.right)
            
            # Store this sum to check later
            subtree_sums.append(current_sum)
            return current_sum

        # 1. Calculate total sum (it will be the last element added or return value)
        total_sum = get_sums(root)
        
        # 2. Find the max product
        max_prod = 0
        for s in subtree_sums:
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product
        
        # 3. Return modulo 10^9 + 7
        return max_prod % (10**9 + 7)