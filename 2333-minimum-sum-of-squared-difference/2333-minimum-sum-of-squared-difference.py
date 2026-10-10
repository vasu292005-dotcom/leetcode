class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        diff = sorted([abs(a - b) for a, b in zip(nums1, nums2)], reverse=True)
        k = k1 + k2
        if sum(diff) <= k:
            return 0
        diff.append(0)
        for i in range(len(nums1)):
            cost = (diff[i] - diff[i + 1]) * (i + 1)
            if k >= cost:
                k -= cost
            else:
                level, rem = divmod(k, i + 1)
                target = diff[i] - level
                return sum(x * x for x in diff[i + 1:]) + rem * (target - 1) ** 2 + (i + 1 - rem) * target ** 2
        return 0