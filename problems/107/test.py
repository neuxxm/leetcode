# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:54-00:02
class Solution(object):
    def levelOrderBottom(self, root):
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
            t,lvl = q.pop(0)
            if lvl < len(rs):
                rs[0].append(t.val)
            else:
                rs.insert(0, [])
                rs[0].append(t.val)
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
        return rs
