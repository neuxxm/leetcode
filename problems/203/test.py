# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#14:58-14:59
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        tmp = ListNode(0)
        tmp.next = head
        last = tmp
        p = head
        while p:
            if p.val == val:
                last.next = p.next
            else:
                last = p
            p = p.next
        return tmp.next
