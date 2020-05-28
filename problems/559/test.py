"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#12:21-12:22
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        r = 1
        for child in root.children:
            r = max(r, self.maxDepth(child) + 1)
        return r
