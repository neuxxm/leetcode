# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#16:49-16:51
class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        p2 = head
        while k > 0 and p2:
            p2 = p2.next
            k -= 1
        while p and p2:
            p = p.next
            p2 = p2.next
        return p
