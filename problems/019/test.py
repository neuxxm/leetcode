# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#20:01AC
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        while n > 1:
            n -= 1
            p = p.next
        last = None
        p2 = head
        while True:
            p = p.next
            if p == None:
                break
            last = p2
            p2 = p2.next
        if last:
            last.next = p2.next
        else:
            head = head.next
        return head
