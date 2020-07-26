# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#20:31-20:35
def f(x, zs):
    if x == None:
        return
    if x.left == None and x.right == None:
        zs.append(x.val)
    f(x.left, zs)
    f(x.right, zs)
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        q = []
        q2 = []
        f(root1, q)
        f(root2, q2)
        n = len(q)
        m = len(q2)
        if n != m:
            return False
        for i in xrange(n):
            if q[i] != q2[i]:
                return False
        return True
