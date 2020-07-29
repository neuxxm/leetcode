# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#17:09-17:27
def f(last, head, t):
    if head:
        last.next = ListNode(t)
        last = last.next
    else:
        head = ListNode(t)
        last = head
    return last, head
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        last = None
        i = l1
        j = l2
        tag = 0
        while i and j:
            t = i.val + j.val + tag
            if t >= 10:
                t -= 10
                tag = 1
            else:
                tag = 0
            i = i.next
            j = j.next
            last, head = f(last, head, t)
        while i:
            t = i.val + tag
            if t >= 10:
                t -= 10
                tag = 1
            else:
                tag = 0
            i = i.next
            last, head = f(last, head, t)
        while j:
            t = j.val + tag
            if t >= 10:
                t -= 10
                tag = 1
            else:
                tag = 0
            j = j.next
            last, head = f(last, head, t)
        if tag:
            last, head = f(last, head, tag)
        return head
