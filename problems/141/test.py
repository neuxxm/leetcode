# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#13:39fail
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        p2 = head
        while p:
            p = p.next
            if p == None:
                break
            p = p.next
            if p == None:
                break
            p2 = p2.next
            if p2 == p:
                return True
        return False
