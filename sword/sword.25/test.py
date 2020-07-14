# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#15:50-16:02
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        h = None
        head = None
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                if h == None:
                    h = ListNode(p1.val)
                    head = h
                else:
                    h.next = p1
                    h = h.next
                p1 = p1.next
            else:
                if h == None:
                    h = ListNode(p2.val)
                    head = h
                else:
                    h.next = p2
                    h = h.next
                p2 = p2.next
        while p1 != None:
            if h == None:
                h = ListNode(p1.val)
                head = h
            else:
                h.next = p1
                h = h.next
            p1 = p1.next
        while p2 != None:
            if h == None:
                h = ListNode(p2.val)
                head = h
            else:
                h.next = p2
                h = h.next
            p2 = p2.next
        return head
