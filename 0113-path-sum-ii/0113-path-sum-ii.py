# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val

            if not node.left and not node.right and total == targetSum:
                result.append(path[:])

            dfs(node.left, path, total)
            dfs(node.right, path, total)

            path.pop()

        dfs(root, [], 0)
        return result