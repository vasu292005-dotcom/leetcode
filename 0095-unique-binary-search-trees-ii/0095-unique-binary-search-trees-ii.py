# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        def build(left,right):
            if left>right:
                return [None]
            ans=[]
            for i in range(left,right+1):
                for l in build(left,i-1):
                    for r in build(i+1,right):
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        ans.append(root)
            return ans
        return build(1,n)