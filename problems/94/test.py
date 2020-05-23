# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = []
        cur = root
        r = []
        while cur or len(q) > 0:
            while cur:
                q.append(cur)
                cur = cur.left
            if len(q) > 0:
                cur = q.pop()
                r.append(cur.val)
                cur = cur.right
        return r
