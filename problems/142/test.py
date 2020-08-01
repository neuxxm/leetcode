# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#10:35fail
def get_inter(head):
    p = head
    p2 = head
    while True:
        p2 = p2.next
        if p2 == None:
            return None
        p2 = p2.next
        if p2 == None:
            return None
        p = p.next
        if p == p2:
            return p
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        x = get_inter(head)
        if x == None:
            return None
        p = head
        while True:
            if p == x:
                return p
            p = p.next
            x = x.next
