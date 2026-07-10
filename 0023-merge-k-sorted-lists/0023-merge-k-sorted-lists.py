# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        from heapq import heappush, heappop
        heap = []
        for head in lists:
            if head:
                heappush(heap, (head.val, head))
        dummy = ListNode(-1)
        p = dummy
        while heap:
            cur = heappop(heap)[1]
            p.next = ListNode(cur.val)
            p = p.next
            if cur.next:
                heappush(heap, (cur.next.val, cur.next))
        return dummy.next