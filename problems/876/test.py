# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#23:18-23:21
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p = head
        p2 = head.next
        if p2 == None:
            return p
        while True:
            p = p.next
            if p == None:
                break
            p2 = p2.next
            if p2 == None:
                break
            p2 = p2.next
            if p2 == None:
                break
        return p
