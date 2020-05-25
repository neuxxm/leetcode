# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#13:24-13:34
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = []
        q.append((root, 0, 1))
        rs = []
        rs_cnt = 0
        r = 0
        while len(q) > 0:
            t,lvl,ix = q.pop(0)
            if lvl < rs_cnt:
                rs.append(ix)
            else:
                if len(rs) > 0:
                    z = rs[len(rs)-1] - rs[0] + 1
                    if z > r:
                        r = z
                rs = []
                rs.append(ix)
                rs_cnt += 1
            if t.left:
                q.append((t.left, lvl+1, (ix<<1)))
            if t.right:
                q.append((t.right, lvl+1, (ix<<1)+1))
        if len(rs) > 0:
            z = rs[len(rs)-1] - rs[0] + 1
            if z > r:
                r = z
        return r
