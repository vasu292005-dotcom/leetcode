class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        best = 0
        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            if area > best:
                best = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best