class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        a=1
        b=1
        for i in range(1,len(s)):
            cur=0
            if s[i]!='0':
                cur+=b
            if 10<=int(s[i-1:i+1])<=26:
                cur+=a
            a=b
            b=cur
        return b