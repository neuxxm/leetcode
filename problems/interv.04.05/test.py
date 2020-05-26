# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#12:08-12:27
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        cur = root
        last = float('-inf')
        while cur:
            if cur.left:
                p = cur.left
                while p.right and p.right != cur:
                    p = p.right
                if p.right:
                    if cur.val <= last:
                        return False
                    last = cur.val
                    p.right = None
                    cur = cur.right
                else:
                    p.right = cur
                    cur = cur.left
            else:
                if cur.val <= last:
                    return False
                last = cur.val
                cur = cur.right
        return True
