# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:08fail
class Solution(object):
    def postorderTraversal(self, root):
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
            if t:
                if t.left or t.right:
                    q.append(t)
                    q.append(None)
                    if t.right:
                        q.append(t.right)
                    if t.left:
                        q.append(t.left)
                else:
                    r.append(t.val)
            else:
                t = q.pop()
                r.append(t.val)
        return r