class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = set()
        diag1 = set()
        diag2 = set()
        count = [0]
        def dfs(row):
            if row == n:
                count[0] += 1
                return
            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                dfs(row + 1)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        dfs(0)
        return count[0]