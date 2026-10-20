class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sorted(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            for st in range(0, n, k):
                b = nums[st:st + k]
                d = 0
                for i in range(k):
                    if b[i] > b[(i + 1) % k]:
                        d += 1
                if d > 1 or sorted(b) != s[st:st + k]:
                    ok = False
                    break
            if ok:
                total += k
        return total