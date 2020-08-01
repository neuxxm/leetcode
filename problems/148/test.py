# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#13:09fail
def get_mid(x):
    p2 = x
    p = x
    while True:
        p2 = p2.next
        if p2 == None:
            return p
        p2 = p2.next
        if p2 == None:
            return p
        p = p.next
    return p
def update(z, last, v):
    if last:
        last.next = ListNode(v)
        last = last.next
    else:
        z = ListNode(v)
        last = z
    return z, last
def mergesort(head):
    if head.next == None:
        return head
    m = get_mid(head)
    p = head
    p2 = m.next
    m.next = None
    m1 = mergesort(p)
    m2 = mergesort(p2)
    i = m1
    j = m2
    z = None
    last = None
    while i and j:
        if i.val < j.val:
            z, last = update(z, last, i.val)
            i = i.next
        else:
            z, last = update(z, last, j.val)
            j = j.next
    while i:
        z, last = update(z, last, i.val)
        i = i.next
    while j:
        z, last = update(z, last, j.val)
        j = j.next
    return z
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        return mergesort(head)
