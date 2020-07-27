#20:30-20:40
def f(x, lvl, path, p, z):
    path[lvl] = x
    if x.left:
        if f(x.left, lvl+1, path, p, z):
            return True
    if x.right:
        if f(x.right, lvl+1, path, p, z):
            return True
    if x.val == p:
        z.append(path[:lvl+1])
        return True
    return False
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        az = []
        path = [0] * 10005
        f(root, 0, path, p.val, az)
        bz = []
        f(root, 0, path, q.val, bz)
        a = az[0]
        b = bz[0]
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        while i < n and j < m:
            if a[i].val == b[j].val:
                i += 1
                j += 1
            else:
                break
        return a[i-1]
