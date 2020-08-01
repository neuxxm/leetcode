# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#10:07-10:16
#h -> b -> a
#c
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        p = head
        while p != None:
            t = p.next
            p.next = h.next
            h.next = p
            p = t
        return h.next
