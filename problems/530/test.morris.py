# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#22:23-22:32
def f(x, last, mi):
    if last != None:
        t = x - last
        if t < mi:
            mi = t
        last = x
    else:
        last = x
    return last, mi
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        last = None
        mi = float('inf')
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right and p.right != cur:
                    p = p.right
                if p.right:
                    last, mi = f(cur.val, last, mi)
                    p.right = None
                    cur = cur.right
                else:
                    p.right = cur
                    cur = cur.left
            else:
                last, mi = f(cur.val, last, mi)
                cur = cur.right
        return mi
