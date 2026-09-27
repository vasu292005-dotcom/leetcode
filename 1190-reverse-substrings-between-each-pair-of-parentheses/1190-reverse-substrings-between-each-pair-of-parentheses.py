class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr = ""

        for c in s:
            if c == "(":
                stack.append(curr)
                curr = ""
            elif c == ")":
                curr = curr[::-1]
                curr = stack.pop() + curr
            else:
                curr += c

        return curr