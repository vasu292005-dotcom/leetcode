class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and value[s[i]] < value[s[i + 1]]:
                total -= value[s[i]]
            else:
                total += value[s[i]]
        return total