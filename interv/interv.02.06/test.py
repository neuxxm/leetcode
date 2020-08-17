# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#21:13
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        if n < 2:
            return True
        m = n / 2
        p = head
        n = 0
        mid = None
        while p:
            n += 1
            if n == m:
                mid = p
                break
            p = p.next
        p2 = p.next
        while p2:
            t = p2.next
            p2.next = mid.next
            mid.next = p2
            p2 = t
        p = head
        p2 = mid
        cnt = 0
        while p and p2:
            if p.val != p2.val:
                return False
            p = p.next
            p2 = p2.next
            cnt += 1
        return cnt == m-1 or cnt == m
