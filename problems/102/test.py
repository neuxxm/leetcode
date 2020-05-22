# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = []
        q.append((root, 0))
        rs = []
        while len(q) > 0:
            t, lvl = q.pop(0)
            if lvl < len(rs):
                rs[lvl].append(t.val)
            else:
                rs.append([])
                rs[lvl].append(t.val)
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
        return rs
