# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#10:04-10:12
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        a = inorder
        b = postorder
        if len(a) == 0:
            return None
        if len(a) == 1:
            return TreeNode(a[0])
        n = len(a)
        r = TreeNode(b[n-1])
        ix = a.index(b[n-1])
        r.left = self.buildTree(a[:ix], b[:ix])
        r.right = self.buildTree(a[ix+1:], b[ix:-1])
        return r
