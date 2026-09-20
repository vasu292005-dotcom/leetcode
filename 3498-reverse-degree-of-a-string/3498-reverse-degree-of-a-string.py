class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for i, ch in enumerate(s, 1):
            value = ord('z') - ord(ch) + 1
            total += value * i

        return total