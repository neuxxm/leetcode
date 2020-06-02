#13:13-13:27
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        cur = head
        while cur != None:
            z = cur.next
            cur.next = h.next
            h.next = cur
            cur = z
        return h.next
