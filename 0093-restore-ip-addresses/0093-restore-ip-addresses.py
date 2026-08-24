class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans=[]
        def backtrack(start,path):
            if len(path)==4:
                if start==len(s):
                    ans.append(".".join(path))
                return
            for i in range(start,min(start+3,len(s))):
                part=s[start:i+1]
                if len(part)>1 and part[0]=='0':
                    break
                if int(part)>255:
                    break
                backtrack(i+1,path+[part])
        backtrack(0,[])
        return ans