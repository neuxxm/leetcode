# Definition for singly-linked list.
#12:29-12:45
def check(x, head):
    if head == None:
        return True
    if x == None:
        return head == None
    if x.val != head.val:
        return False
    if check(x.left, head.next):
        return True
    if check(x.right, head.next):
        return True
    return False
def f(x, head):
    if x.left:
        if f(x.left, head):
            return True
    if x.right:
        if f(x.right, head):
            return True
    if check(x, head):
        return True
    return False
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        return f(root, head)
