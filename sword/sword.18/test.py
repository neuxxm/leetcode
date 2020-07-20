# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#0:10-0:12
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            return head.next
        last = head
        p = head.next
        while p:
            if p.val == val:
                last.next = p.next
                return head
            last = p
            p = p.next
        return head
