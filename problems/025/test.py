#13:54-15:01
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def judge(cur, k):
    r = 0
    t = cur
    while t != None:
        r += 1
        t = t.next
    return r >= k
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        h = ListNode(0)
        t = ListNode(0)
        cur = head
        cnt = 0
        h2 = ListNode(0)
        while cur:
            if cnt == 0 and not judge(cur, k):
                t.next.next = cur
                break
            z = cur.next
            if h.next == None:
                t.next = cur
            cur.next = h.next
            h.next = cur
            cnt += 1
            if cnt == k:
                cnt = 0
                if h2.next == None:
                    h2.next = h.next
                h = t.next
            cur = z
        return h2.next
