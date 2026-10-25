class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            if grid[r][c] == 1:
                return 1
            grid[r][c] = 1
            return dfs(r+1, c) & dfs(r-1, c) & dfs(r, c+1) & dfs(r, c-1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += dfs(i, j)
        return count