# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#12:47AC
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p = head.next
        last = head
        cnt = 2
        while p:
            if (cnt&1) == 0:
                t = last.val
                last.val = p.val
                p.val = t
            cnt += 1
            last = p
            p = p.next
        return head
