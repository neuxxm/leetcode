"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#17:20-17:22
class Solution(object):
    def postorder(self, root):
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
                q.append(x)
                q.append(None)
                for c in x.children[::-1]:
                    q.append(c)
            else:
                x = q.pop()
                r.append(x.val)
        return r
