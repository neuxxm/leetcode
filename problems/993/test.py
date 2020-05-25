# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#12:49-13:09
def f(root, lvl, x, y, r):
    if root.left:
        if root.left.val == x or root.left.val == y:
            if r[0] == -1:
                r[0] = lvl
                r[1] = root.val
            else:
                if lvl != r[0]:
                    return False
                if root.val == r[1]:
                    return False
                return True
        if f(root.left, lvl+1, x, y, r):
            return True
    if root.right:
        if root.right.val == x or root.right.val == y:
            if r[0] == -1:
                r[0] = lvl
                r[1] = root.val
            else:
                if lvl != r[0]:
                    return False
                if root.val == r[1]:
                    return False
                return True
        if f(root.right, lvl+1, x, y, r):
            return True
    return False
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        r = [-1, -1]
        return f(root, 0, x, y, r)
