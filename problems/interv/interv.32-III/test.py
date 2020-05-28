# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#12:02-12:05
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
        r = []
        cnt = 0
        while len(q) > 0:
            t, lvl = q.pop(0)
            if lvl < cnt:
                r.append(t.val)
            else:
                n = len(r)
                if n > 0:
                    if cnt&1:
                        rs.append(r)
                    else:
                        rs.append(r[::-1])
                r = []
                r.append(t.val)
                cnt += 1
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
        n = len(r)
        if n > 0:
            if cnt&1:
                rs.append(r)
            else:
                rs.append(r[::-1])
        return rs
