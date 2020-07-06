# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#15:01fail
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        p2 = headB
        if p == None or p2 == None:
            return None
        cnt = 0
        cnt2 = 0
        while p != p2:
            if p.next:
                p = p.next
            else:
                cnt += 1
                if cnt >= 2:
                    p = None
                    break
                p = headB
            if p2.next:
                p2 = p2.next
            else:
                p2 = headA
        return p
