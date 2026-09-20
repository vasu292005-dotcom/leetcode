# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        position = {}

        for i in range(len(inorder)):
            position[inorder[i]] = i

        index = [len(postorder) - 1]

        def build(left, right):
            if left > right:
                return None

            value = postorder[index[0]]
            index[0] -= 1

            root = TreeNode(value)

            mid = position[value]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)