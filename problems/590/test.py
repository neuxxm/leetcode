"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        q = []
        q.append(root)
        r = []
        while len(q) > 0:
            t = q.pop()
            r.append(t.val)
            for c in t.children:
                q.append(c)
        return r[::-1]
