# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], current_sum: int, target_sum: int) -> bool:
            if node is None:
                return False
            if node.left is None and node.right is None and node.val + current_sum == target_sum:
                return True
            return dfs(node.left, node.val + current_sum, target_sum) or dfs(node.right, node.val + current_sum, target_sum)
        return dfs(root, 0, targetSum)