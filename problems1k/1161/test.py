# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#15:17-15:20
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        q.append(root)
        ma = 0
        ma_ix = 0
        ix = 0
        while q:
            list = []
            s = 0
            while q:
                x = q.pop()
                list.append(x)
                s += x.val
            ix += 1
            if ix == 1:
                ma = s
                ma_ix = ix
            else:
                if s > ma:
                    ma = s
                    ma_ix = ix
            for l in list:
                if l.left:
                    q.append(l.left)
                if l.right:
                    q.append(l.right)
        return ma_ix
