class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(start, total, path):
            if total == target:
                ans.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, total + candidates[i], path)
                path.pop()
        dfs(0, 0, [])
        return ans