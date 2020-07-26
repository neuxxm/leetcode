"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#17:13-17:15
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        q = [root]
        r = []
        while q:
            x = q.pop()
            if x:
                for c in x.children[::-1]:
                    q.append(c)
                q.append(x)
                q.append(None)
            else:
                x = q.pop()
                r.append(x.val)
        return r
