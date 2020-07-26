# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#17:27-18:32
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = [(root,0,0)]
        rs = []
        while q:
            xs = []
            while q:
                x,r,c = q.pop(0)
                xs.append((x,r,c))
                rs.append((c,r,x.val))
            for x,r,c in xs:
                if x.left:
                    q.append((x.left,r+1,c-1))
                if x.right:
                    q.append((x.right,r+1,c+1))
        zs = []
        rs1 = sorted(rs)
        bias = -rs1[0][0]+1
        for r,c,x in rs1:
            r += bias
            while len(zs) < r:
                zs.append([])
            zs[r-1].append(x)
        return zs
