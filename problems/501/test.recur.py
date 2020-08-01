# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#18:14-18:31
def f(x, z):
    if x == None:
        return
    f(x.left, z)
    if z[0] != None:
        if x.val == z[0]:
            z[1] += 1
        else:
            if z[1] > z[3]:
                z[2] = [z[0]]
                z[3] = z[1]
            elif z[1] == z[3]:
                z[2].append(z[0])
            z[0] = x.val
            z[1] = 1
    else:
        z[0] = x.val
        z[1] = 1
    f(x.right, z)
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        z = [None, 0, [], 0]
        f(root, z)
        if z[1] > z[3]:
            z[2] = [z[0]]
            z[3] = z[1]
        elif z[1] == z[3]:
            z[2].append(z[0])
        return z[2]
