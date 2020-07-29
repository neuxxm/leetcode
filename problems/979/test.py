# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#10:53fail 无思路
def need(x, z):
    if x == None:
        return 0
    l = need(x.left, z)
    r = need(x.right, z)
    t = abs(l) + abs(r)
    z[0] += t
    return x.val+l+r-1
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        z = [0]
        need(root, z)
        return z[0]
