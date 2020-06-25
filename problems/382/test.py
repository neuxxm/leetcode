# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#23:08-23:18
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        #k=1000 ans = 1000/1001
        #1000/1001 * 1
        i = 0
        p = self.head
        ans = self.head.val
        while p:
            i += 1
            r = random.randint(1, i)
            if r <= 1:
                ans = p.val
            p = p.next
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
