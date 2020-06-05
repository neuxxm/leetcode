#22:35-22:45
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        cnt = 0
        while cur != None:
            if cur.right:
                p = cur.right
                while p.left != None and p.left != cur:
                    p = p.left
                if p.left:
                    cnt += cur.val
                    cur.val = cnt
                    p.left = None
                    cur = cur.left
                else:
                    p.left = cur
                    cur = cur.right
            else:
                cnt += cur.val
                cur.val = cnt
                cur = cur.left
        return root
