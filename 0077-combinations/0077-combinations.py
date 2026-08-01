class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(start, path):
            if len(path) == k:
                ans.append(path[:])
                return
            for num in range(start, n + 1):
                path.append(num)
                dfs(num + 1, path)
                path.pop()
        dfs(1, [])
        return ans