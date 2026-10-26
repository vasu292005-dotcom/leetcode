class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    stack = [(i, j)]
                    total = 0
                    grid[i][j] = -grid[i][j]
                    while stack:
                        x, y = stack.pop()
                        total -= grid[x][y]
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                                stack.append((nx, ny))
                                grid[nx][ny] = -grid[nx][ny]
                    if total % k == 0:
                        ans += 1
        return ans