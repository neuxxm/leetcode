# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#20:53-21:10
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        last = head
        if head.next == None:
            return head
        p = head.next
        ans = p
        zz = None
        while True:
            if zz:
                zz.next = p
            t = p.next
            p.next = last
            last.next = t
            if t == None:
                break
            zz = last
            last = t
            if t.next == None:
                break
            p = t.next
        return ans
