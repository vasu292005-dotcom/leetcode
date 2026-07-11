class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                ans = solve(i, j + 2) or (match and solve(i + 1, j))
            else:
                ans = match and solve(i + 1, j + 1)
            memo[(i, j)] = ans
            return ans
        return solve(0, 0)