# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#22:55-23:01
class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        p = head
        p2 = head
        while k > 0:
            k -= 1
            p2 = p2.next
        if p2 == None:
            return p.val
        while True:
            p2 = p2.next
            p = p.next
            if p2 == None:
                break
        return p.val
