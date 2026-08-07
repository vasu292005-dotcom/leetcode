# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                value = head.val
                while head and head.val == value:
                    head = head.next
                prev.next = head
            else:
                prev = head
                head = head.next
        return dummy.next