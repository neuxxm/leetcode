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
#12:31-12:42
def hit(path, lvl, buf):
    s = ''.join(path[:lvl+1])
    return s.find(buf) != -1
def f(x, lvl, path, buf):
    path[lvl] = '%d'%x.val
    if x.left == None and x.right == None:
        return hit(path, lvl, buf)
    if x.left:
        if f(x.left, lvl+1, path, buf):
            return True
    if x.right:
        if f(x.right, lvl+1, path, buf):
            return True
    return False
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        path = [''] * 2505
        buf = ''
        while head:
            buf += '%d'%head.val
            head = head.next
        return f(root, 0, path, buf)
