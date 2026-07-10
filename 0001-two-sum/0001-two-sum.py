class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for index in range(len(nums)):
            current = nums[index]
            required = target - current

            if required in seen:
                return [seen[required], index]

            seen[current] = index

        return []