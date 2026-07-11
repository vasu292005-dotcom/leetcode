class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone = {
            "2":"abc","3":"def","4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        ans = [""]
        for digit in digits:
            temp = []
            for prefix in ans:
                for ch in phone[digit]:
                    temp.append(prefix + ch)
            ans = temp
        return ans