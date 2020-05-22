# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        q = []
        q.append(root)
        rs = []
        while len(q) > 0:
            t = q.pop()
            rs.append(t.val)
            if t.right:
                q.append(t.right)
            if t.left:
                q.append(t.left)
        return rs
