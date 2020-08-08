#8.8 15:27-19:04
def f(x, z):
    if x == None:
        return
    f(x.left, z)
    if z[0] != None:
        if x.val < z[0].val:
            if z[1] == 0:
                z[1] += 1
                z[2] = z[0]
                z[3] = x
            else:
                z[3] = x
        z[0] = x
    else:
        z[0] = x
    f(x.right, z)
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        z = [None, 0, None, None]
        f(root, z)
        t = z[2].val
        z[2].val = z[3].val
        z[3].val = t
