# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:25-19:38
def f(x, z):
    if x == None:
        return 0
    l = f(x.left, z)
    r = f(x.right, z)
    t = 1
    if x.left and x.left.val == x.val:
        t += l
    else:
        l = 0
    if x.right and x.right.val == x.val:
        t += r
    else:
        r = 0
    if t > z[0]:
        z[0] = t
    return max(l, r) + 1
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        z = [0]
        f(root, z)
        return z[0]-1
