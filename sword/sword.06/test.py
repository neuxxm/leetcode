# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#16:38-16:38
class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        p = head
        r = []
        while p:
            r.append(p.val)
            p = p.next
        return r[::-1]
