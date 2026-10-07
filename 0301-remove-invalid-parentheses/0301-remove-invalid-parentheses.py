class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        left = right = 0

        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        ans = set()
        def dfs(i, left_rem, right_rem, balance, path):
            if i == len(s):
                if left_rem == 0 and right_rem == 0 and balance == 0:
                    ans.add(''.join(path))
                return

            c = s[i]

            if c == '(':
                if left_rem > 0:
                    dfs(i + 1, left_rem - 1, right_rem, balance, path)

                path.append(c)
                dfs(i + 1, left_rem, right_rem, balance + 1, path)
                path.pop()

            elif c == ')':
                if right_rem > 0:
                    dfs(i + 1, left_rem, right_rem - 1, balance, path)

                if balance > 0:
                    path.append(c)
                    dfs(i + 1, left_rem, right_rem, balance - 1, path)
                    path.pop()

            else:
                path.append(c)
                dfs(i + 1, left_rem, right_rem, balance, path)
                path.pop()

        dfs(0, left, right, 0, [])

        return list(ans)