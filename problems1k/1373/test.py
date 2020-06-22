# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#18:57fail
def is_bst(x, z):
    if x == None:
        return True, 0
    sam = x.val
    if x.left:
        p = x.left    
        while p.right:
            p = p.right
        lval = p.val
    else:
        lval = float('-inf')
    if x.right:
        p = x.right
        while p.left:
            p = p.left
        rval = p.val
    else:
        rval = float('inf')
    #print x.val, lval ,rval
    b = lval < x.val and x.val < rval
    b2, sam2 = is_bst(x.left, z)
    b3, sam3 = is_bst(x.right, z)
    if b and b2 and b3:
        if sam+sam2+sam3 > z[0]:
            z[0] = sam+sam2+sam3
    return b and b2, sam+sam2+sam3
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        z = [0]
        is_bst(root, z)
        return z[0]
