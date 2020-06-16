#19:53
import random
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        p = self.head
        i = 0
        z = 0
        while p:
            i += 1
            # 1000/1001=k/i
            r = random.randint(1, i)
            if r <= 1:
            # 1/1000=1/k
                z = p.val
            p = p.next
        return z
