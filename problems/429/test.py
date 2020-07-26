"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#17:01-17:04
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return
        q = [root]
        rs = []
        while q:
            xs = []
            while q:
                xs.append(q.pop(0))
            r = []
            for x in xs:
                r.append(x.val)
            rs.append(r)
            for x in xs:
                for c in x.children:
                    q.append(c)
        return rs
