# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#22:50-22:52
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        q = []
        q.append((root, 0))
        r = []
        rs = []
        cnt = 0
        while len(q) > 0:
            t, lvl = q.pop(0)
            if lvl < cnt:
                r.append(t.val)
            else:
                if len(r) > 0:
                    rs.append(max(r))
                r = []
                r.append(t.val)
                cnt += 1
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
        if len(r) > 0:
            rs.append(max(r))
        return rs
