# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        a = preorder
        if len(a) == 0:
            return None
        b = inorder
        r = TreeNode(a[0])
        ix = b.index(a[0])
        r.left = self.buildTree(a[1:ix+1], b[:ix])
        r.right = self.buildTree(a[ix+1:], b[ix+1:])
        return r
