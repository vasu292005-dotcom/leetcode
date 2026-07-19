# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        p = head
        l = 1
        while p.next:
            p = p.next
            l += 1
        p.next = head
        p = head
        t = l - k % l
        for _ in range(t - 1):
            p = p.next
        ans = p.next
        p.next = None
        return ans