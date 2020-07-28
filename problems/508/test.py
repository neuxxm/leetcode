# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#13:49-13:55
from collections import defaultdict
def f(x, z):
    if x == None:
        return 0
    l = f(x.left, z)
    r = f(x.right, z)
    t = x.val + l + r
    z[t] += 1
    return t
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        z = defaultdict(lambda:0)
        f(root, z)
        ma = 0
        for v in z.values():
            if v > ma:
                ma = v
        rs = []
        for k,v in z.items():
            if v == ma:
                rs.append(k)
        return rs
