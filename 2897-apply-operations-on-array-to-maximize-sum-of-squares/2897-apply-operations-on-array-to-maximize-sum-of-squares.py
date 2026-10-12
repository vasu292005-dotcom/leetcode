class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        cnt = [0] * 32
        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    cnt[b] += 1
        res = 0
        for _ in range(k):
            x = 0
            for b in range(32):
                if cnt[b] > 0:
                    x |= 1 << b
                    cnt[b] -= 1
            res = (res + x * x) % MOD
        return res