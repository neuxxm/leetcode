# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#10:22-10:26
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        p = head
        p2 = head
        while True:
            p2 = p2.next
            if p2 == None:
                return False
            p2 = p2.next
            if p2 == None:
                return False
            if p2 == p:
                return True
            p = p.next
