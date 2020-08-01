# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#11:35-11:54
from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        p = [None] * n
        for i in xrange(n):
            p[i] = lists[i]
        z = None
        last = None
        q = []
        for i in xrange(n):
            if p[i]:
                heappush(q, (p[i].val, p[i]))
        while q:
            val,mip = heappop(q)
            if last != None:
                last.next = ListNode(val)
                last = last.next
            else:
                z = ListNode(val)
                last = z
            if mip.next:
                heappush(q, (mip.next.val,mip.next))
        return z
