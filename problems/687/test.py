#16:19-16:39
def f(x, z):
    lsame = 0
    rsame = 0
    l = 0
    r = 0
    if x.left:
        t = f(x.left, z)
        if x.val == x.left.val:
            lsame = 1
            l = t
    if x.right:
        t = f(x.right, z)
        if x.val == x.right.val:
            rsame = 1
            r = t
    ans = 0
    if lsame or rsame:
        ans = max(l+1, r+1)
        if ans > z[0]:
            z[0] = ans
    if lsame and rsame:
        t = l + r + 2
        if t > z[0]:
            z[0] = t
    return ans
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
        return z[0]
