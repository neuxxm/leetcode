"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#16:44
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        q = []
        q.append((root,0))
        rcnt = 0
        last = None
        while len(q) > 0:
            t, lvl = q.pop(0)
            if lvl < rcnt:
                last.next = t
                last = t
            else:
                last = t
                rcnt += 1
            if t.left:
                q.append((t.left, lvl+1))
            if t.right:
                q.append((t.right, lvl+1))
