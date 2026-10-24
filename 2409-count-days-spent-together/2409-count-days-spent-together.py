class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def convert(date):
            month, day = map(int, date.split('-'))
            return sum(months[:month - 1]) + day

        start = max(convert(arriveAlice), convert(arriveBob))
        end = min(convert(leaveAlice), convert(leaveBob))

        return max(0, end - start + 1)