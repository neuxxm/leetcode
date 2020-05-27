# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def f(head):
    p = head
    cnt = 0
    while p:
        cnt += 1
        if cnt > 2:
            break
        p = p.next
    if cnt <= 2:
        return cnt, None, None, None
    p = head
    p2 = head.next
    last = None
    while True:
        last = p
        p = p.next
        if p2.next and p2.next.next:
            p2 = p2.next.next
        else:
            break
    return 3, last, p, p.next
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        p = head
        cnt, last, mid, mid2 = f(head)
        r = None
        if cnt == 1:
            r = TreeNode(head.val)
        elif cnt == 2:
            r = TreeNode(head.next.val)
            r.left = TreeNode(head.val) 
        elif mid:
            r = TreeNode(mid.val)
            if last:
                last.next = None
            r.left = self.sortedListToBST(p)
            r.right = self.sortedListToBST(mid2)
        return r
