# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def BSTSequences(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def f(cur, q, path, rs):
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            q_len = len(q)
            if q_len == 0:
                rs.append(path[:])
                return
            for i in xrange(q_len):
                t = q[i]
                q2 = q[:i] + q[i+1:]
                f(t, q2, path + [t.val], rs)
        if root == None:
            return [[]]
        q = []
        rs = []
        f(root, q, [root.val], rs)
        return rs
