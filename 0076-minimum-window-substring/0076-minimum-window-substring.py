class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        required = len(need)
        formed = 0
        window = {}
        left = 0
        start = 0
        length = float("inf")
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                formed += 1
            while formed == required:
                if right - left + 1 < length:
                    length = right - left + 1
                    start = left
                ch = s[left]
                window[ch] -= 1
                if ch in need and window[ch] < need[ch]:
                    formed -= 1
                left += 1
        if length == float("inf"):
            return ""
        return s[start:start + length]