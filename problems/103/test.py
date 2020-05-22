# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:42-23:49
class Solution(object):
    def zigzagLevelOrder(self, root):
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
                if lvl&1:
                    rs[lvl].insert(0, t.val)
                else:
                    rs[lvl].append(t.val)
            else:
                rs.append([])
                rs[lvl].append(t.val)
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
        return rs
