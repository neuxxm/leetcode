# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:48-23:51
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        q = []
        q.append((root, 0))
        r = []
        cnt = 0
        rs = []
        while len(q):
            t, lvl = q.pop(0)
            if lvl < cnt:
                r.append(t.val)
            else:
                if len(r) > 0:
                    rs.append(float(sum(r)) / len(r))
                r = []
                r.append(t.val)
                cnt += 1
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
        if len(r) > 0:
            rs.append(float(sum(r)) / len(r))
        return rs
