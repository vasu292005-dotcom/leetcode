class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=lambda x: x * x)
        return sum(x * x for x in nums[len(nums)//2:]) - sum(x * x for x in nums[:len(nums)//2])