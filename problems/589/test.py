"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#21:57-21:59
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        q = []
        r = []
        q.append(root)
        while len(q) > 0:
            t = q.pop()
            r.append(t.val)
            child_len = len(t.children)
            for i in xrange(child_len-1, -1, -1):
                q.append(t.children[i])
        return r
