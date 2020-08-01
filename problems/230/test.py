# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#17:23-17:27
def f(x, z, k):
    if x == None:
        return False
    if f(x.left, z, k):
        return True
    z[0] += 1
    if z[0] == k:
        z[1] = x.val
        return True
    if f(x.right, z, k):
        return True
    return False
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        z = [0, -1]
        f(root, z, k)
        return z[1]
