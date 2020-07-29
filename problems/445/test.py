# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#19:29-20:45
def get_len(x):
    r = 0
    while x:
        r += 1
        x = x.next
    return r
def h(s, tag):
    if s >= 10:
        s -= 10
        tag = 1
    else:
        tag = 0
    return s, tag
def f(r, k, l1, l2, l1_len, l2_len):
    if k == 0:
        s = l1.val + l2.val
        s, tag = h(s, 0)
        r[k] = s
        return tag
    elif l1_len <= k and k < l2_len:
        tag = f(r, k-1, l1, l2.next, l1_len, l2_len)
        s = l2.val + tag
        s, tag = h(s, tag)
        r[k] = s
        return tag
    elif k < l1_len and k < l2_len:
        tag = f(r, k-1, l1.next, l2.next, l1_len, l2_len)
        s = l1.val + l2.val + tag
        s, tag = h(s, tag)
        r[k] = s
        return tag
    else:
        r[k] = f(r, k-1, l1, l2, l1_len, l2_len)
        return r[k]
def g(l1, l2, l1_len, l2_len):
    max_len = l2_len
    r = [0] * (max_len+1)
    f(r, max_len, l1, l2, l1_len, l2_len)
    i = max_len
    while r[i] == 0:
        i -= 1
        if i == -1:
            return ListNode(0)
    head = None
    last = None
    while i >= 0:
        if head:
            last.next = ListNode(r[i])
            last = last.next
        else:
            head = ListNode(r[i])
            last = head
        i -= 1
    return head
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_len = get_len(l1)
        l2_len = get_len(l2)
        if l1_len < l2_len:
            return g(l1, l2, l1_len, l2_len)
        else:
            return g(l2, l1, l2_len, l1_len)
