# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#16:47-16:49
#  1
# 2 3 
#4 5
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
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
                if x.right:
                    q.append(x.right)
                if x.left:
                    q.append(x.left)
            else:
                x = q.pop()
                r.append(x.val)
        return r
