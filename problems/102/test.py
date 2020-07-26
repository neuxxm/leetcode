# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#20:11-20:13
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = [root]
        rs = []
        while q:
            xs = []
            l = []
            while q:
                x = q.pop(0)
                xs.append(x)
                l.append(x.val)
            rs.append(l)
            for x in xs:
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return rs
