# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#22:23fail
def f(x):
    if x == None:
        return [0,0]
    l = f(x.left)
    r = f(x.right)
    dp = [0, 0]
    dp[0] = max(l) + max(r)
    dp[1] = x.val + l[0] + r[0]
    return dp
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(f(root))
