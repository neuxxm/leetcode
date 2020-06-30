# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#14:11-14:14
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        l = 1<<(n-1)
        p = head
        r = 0
        while p:
            r += p.val * l
            l >>= 1
            p = p.next
        return r
