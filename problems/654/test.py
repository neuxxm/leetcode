# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:42-16:45
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        a = nums
        if len(a) == 0:
            return None
        n = len(a)
        ma = a[0]
        ma_ix = 0
        for i in xrange(1, n):
            if a[i] > ma:
                ma = a[i]
                ma_ix = i
        r = TreeNode(a[ma_ix])
        r.left = self.constructMaximumBinaryTree(a[:ma_ix])
        r.right = self.constructMaximumBinaryTree(a[ma_ix+1:])
        return r
