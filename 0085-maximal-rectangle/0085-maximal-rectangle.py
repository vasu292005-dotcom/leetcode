class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        cols = len(matrix[0])
        heights = [0] * cols
        best = 0
        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = []
            for i in range(cols + 1):
                current = heights[i] if i < cols else 0
                while stack and heights[stack[-1]] > current:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    area = h * (i - left - 1)
                    if area > best:
                        best = area
                stack.append(i)
        return best