# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#15:34fail
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        cnt = 0
        p = head
        while p:
            cnt += 1
            p = p.next
        mid = (cnt-1) / 2
        p = head
        cnt = 0
        h = None
        while p:
            if cnt == mid:
                t = p.next
                h = p
                h.next = None
                p = t
            else:
                if h:
                    t = p.next
                    p.next = h.next
                    h.next = p
                    p = t
                else:
                    p = p.next
            cnt += 1
        p = head
        p2 = h.next
        while p2:
            if p.val != p2.val:
                return False
            p = p.next
            p2 = p2.next
        return True
