# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#12:20-13:00
def get_nearmin(h, tail, x):
    last = h
    p = h.next
    while p:
        if x.val > p.val:
            if p == tail:
                return tail
            last = p
            p = p.next
        else:
            break
    return last
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        h = ListNode(0)
        h.next = head
        tail = head
        p = head.next
        head.next = None
        while p:
            near = get_nearmin(h, tail, p)
            t = p.next
            if near == tail:
                p.next = near.next
                near.next = p
                tail = p
            else:
                p.next = near.next
                near.next = p
            p = t
        return h.next
