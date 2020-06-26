# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#23:11-23:14
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        p = head
        while p:
            if last:
                if p.val == last.val:
                    last.next = p.next
                else:
                    last = p
            else:
                last = p
            p = p.next
        return head
