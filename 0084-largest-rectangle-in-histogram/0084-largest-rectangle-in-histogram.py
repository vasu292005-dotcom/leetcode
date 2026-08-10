class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        best = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                area = h * (i - left - 1)
                if area > best:
                    best = area
            stack.append(i)
        heights.pop()
        return best