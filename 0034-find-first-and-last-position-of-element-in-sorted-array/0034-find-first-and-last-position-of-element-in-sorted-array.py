class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bound(first):
            left = 0
            right = len(nums) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    pos = mid
                    if first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return pos
        return [bound(True), bound(False)]