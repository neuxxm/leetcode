# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#23:06-23:30
def f(root, ix, lvl, d):
    if (ix, lvl) not in d:
        d[(ix, lvl)] = [root.val]
    else:
        d[(ix, lvl)].append(root.val)
    if root.left:
        f(root.left, ix-1, lvl-1, d)
    if root.right:
        f(root.right, ix+1, lvl-1, d)
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}
        f(root, 0, 0, d)
        rs = []
        last = None
        cnt = 0
        rs = []
        for k,v in sorted(d.items(), key=lambda fs:fs[0][0]*1001 - fs[0][1]):
            if last != None:
                if k[0] != last:
                    rs.append([])
                    cnt += 1
                    for i in sorted(v):
                        rs[cnt].append(i)
                    last = k[0]
                else:
                    for i in sorted(v):
                        rs[cnt].append(i)
            else:
                rs.append([])
                for i in sorted(v):
                    rs[cnt].append(i)
                last = k[0]
        return rs
