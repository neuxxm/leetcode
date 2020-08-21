#13:35-13:37
def f(x, path, lvl, y, z):
    if x == None:
        return
    path[lvl] = x.val
    f(x.left, path, lvl+1, y, z)
    f(x.right, path, lvl+1, y, z)
    if x.left == None and x.right == None:
        if sum(path[:lvl+1]) == y:
            z.append(path[:lvl+1])
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path = [0] *  10005
        z = []
        f(root, path, 0, sum, z)
        return z
