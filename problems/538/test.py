# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#13:21-13:34
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        last = 0
        while cur:
            if cur.right:
                p = cur.right
                while p.left and p.left != cur:
                    p = p.left
                if p.left:
                    cur.val += last
                    last = cur.val
                    p.left = None
                    cur = cur.left
                else:
                    p.left = cur
                    cur = cur.right
            else:
                cur.val += last
                last = cur.val
                cur = cur.left
        return root
