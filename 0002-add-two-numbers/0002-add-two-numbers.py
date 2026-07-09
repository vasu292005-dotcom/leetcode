# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry = l1.val + carry
                l1 = l1.next
            if l2:
                carry = l2.val + carry
                l2 = l2.next
            if carry >= 10:
                p.next = ListNode(carry - 10)
                carry = 1
            else:
                p.next = ListNode(carry)
                carry = 0
            p = p.next
        return dummy.next