# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#11:01-11:05
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        q.append((root, 0))
        r = []
        cnt = 0
        z = 0
        while len(q) > 0:
            t, lvl = q.pop(0)
            if lvl < cnt:
                r.append(t.val)
            else:
                r = []
                r.append(t.val)
                cnt += 1
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
        if len(r) > 0:
            z = sum(r)
        return z
