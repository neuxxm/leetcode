# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#17:51-17:58
#1 4 3 2 5
#1 3 2 4
def f(x, z):
    if x == None:
        return
    f(x.left, z)
    if z[0] != None:
        if x.val < z[0]:
            if z[2] == None:
                z[2] = z[1]
                z[4] = x
            else:
                z[3] = x
        z[0] = x.val
        z[1] = x
    else:
        z[0] = x.val
        z[1] = x
    f(x.right, z)
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        z = [None, None, None, None, None]
        f(root, z)
        if z[3] == None:
            z[3] = z[4]
        t = z[2].val
        z[2].val = z[3].val
        z[3].val = t
