# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:14-16:17
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        q = []
        q.append(root)
        r = []
        while len(q) > 0:
            t = q.pop()
            if t == None:
                t = q.pop()
                r.append(t.val)
            else:
                if t.right == None and t.left == None:
                    r.append(t.val)
                else:
                    if t.right:
                        q.append(t.right)
                    if t.left:
                        q.append(t.left)
                    q.append(t)
                    q.append(None)
        return r
