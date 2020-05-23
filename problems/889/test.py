# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#9:46-9:56
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        a = pre
        if len(a) == 0:
            return None
        if len(a) == 1:
            return TreeNode(a[0])
        b = post
        r = TreeNode(a[0])
        ix = b.index(a[1])
        r.left = self.constructFromPrePost(a[1:ix+2], b[:ix+1])
        r.right = self.constructFromPrePost(a[ix+2:], b[ix+1:-1])
        return r
