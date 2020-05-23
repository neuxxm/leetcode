"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#21:06-21:10
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = []
        q.append((root, 0))
        r = []
        while len(q) > 0:
            t, lvl = q.pop(0)
            if lvl < len(r):
                r[lvl].append(t.val)
            else:
                r.append([t.val])
            if t.children:
                for c in t.children:
                    q.append((c, lvl+1))
        return r
