# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#10:53-10:56
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        q.append((root, 0))
        rs = []
        cnt = 0
        ans = root.val
        while len(q) > 0:
            t, lvl = q.pop(0)
            if lvl < cnt:
                pass
            else:
                if len(rs) > 0:
                    ans = rs[0]
                rs = []
                rs.append(t.val)
                cnt += 1
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
        if len(rs) > 0:
            ans = rs[0]
        return ans
