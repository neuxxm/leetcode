# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def f(root, s, lvl, r):
    s[lvl] = root.val
    cnt = 0
    if root.left:
        cnt += 1
        f(root.left, s, lvl+1, r)
    if root.right:
        cnt += 1
        f(root.right, s, lvl+1, r)
    if cnt == 0:
        map = {}
        for i in xrange(lvl+1):
            c = s[i]
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        t = 0
        for v in map.values():
            if v&1:
                t += 1
        if t < 2:
            r[0] += 1
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        s = [0] * (1000000 + 5)
        r = [0]
        f(root, s, 0, r)
        return r[0]
