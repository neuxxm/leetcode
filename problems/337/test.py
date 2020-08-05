#8.5 11:46-11:55
def f(x):
    if x == None:
        return [0, 0]
    dp = [0] * 2
    l = f(x.left)
    r = f(x.right)
    dp[0] = max(l[1],l[0]) + max(r[1], r[0])
    dp[1] = x.val + l[0] + r[0]
    return dp
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(f(root))
