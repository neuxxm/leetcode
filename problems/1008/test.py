# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#10:57-11:02
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        a = preorder
        n = len(a)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(a[0])
        r = TreeNode(a[0])
        n = len(a)
        ix = -1
        for i in xrange(1, n):
            if a[i] > a[0]:
                ix = i
                break
        if ix == -1:
            r.left = self.bstFromPreorder(a[1:])
        else:
            r.left = self.bstFromPreorder(a[1:ix])
            r.right = self.bstFromPreorder(a[ix:])
        return r
