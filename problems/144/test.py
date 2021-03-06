# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:34-16:36
#  1
# 2 3
#4 5
#[3,2,1,non]
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
        while q:
            x = q.pop()
            if x:
                if x.right:
                    q.append(x.right)
                if x.left:
                    q.append(x.left)
                q.append(x)
                q.append(None)
            else:
                x = q.pop()
                r.append(x.val)
        return r
