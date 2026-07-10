class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        x *= flag
        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x //= 10
        ans *= flag
        if -2 ** 31 <= ans <= 2 ** 31 - 1:
            return ans
        return 0