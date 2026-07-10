# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        while p1.next and p1.next.next:
            p2 = p1.next
            p3 = p1.next.next
            p1.next = p3
            p2.next = p3.next
            p3.next = p2
            p1 = p1.next.next
        return dummy.next