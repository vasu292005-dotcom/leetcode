class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (x + y + 1) // 2 - cut1
            left1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            right1 = float("inf") if cut1 == x else nums1[cut1]
            left2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            right2 = float("inf") if cut2 == y else nums2[cut2]
            if left1 <= right2 and left2 <= right1:
                if (x + y) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                return float(max(left1, left2))
            if left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1