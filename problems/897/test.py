# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#12:29-12:38
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        last = None
        head = None
        while cur:
            if cur.left:
                p = cur.left
                while p.right and p.right != cur:
                    p = p.right
                if p.right:
                    if last:
                        t = TreeNode(cur.val)
                        last.right = t
                        last = t
                    else:
                        last = TreeNode(cur.val)
                        head = last
                    p.right = None
                    cur = cur.right
                else:
                    p.right = cur
                    cur = cur.left
            else:
                if last:
                    t = TreeNode(cur.val)
                    last.right = t
                    last = t
                else:
                    last = TreeNode(cur.val)
                    head = last
                cur = cur.right
        return head
