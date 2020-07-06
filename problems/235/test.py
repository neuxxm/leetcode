#16:26-19:58
def get_path(root, y, lvl, path, plist):
    if root.val == y.val:
        path[lvl] = root
        plist.append(path[:lvl+1])
        return
    path[lvl] = root
    if root.left:
        get_path(root.left, y, lvl+1, path, plist)
    if root.right:
        get_path(root.right, y, lvl+1, path, plist)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        path = [None] * 100000
        plists = []
        get_path(root, p, 0, path, plists)
        qlists = []
        get_path(root, q, 0, path, qlists)
        plist = plists[0]
        qlist = qlists[0]
        n = len(plist)
        m = len(qlist)
        i = 0
        j = 0
        r = None
        while i < n and j < m:
            if plist[i].val == qlist[j].val:
                r = plist[i]
                i += 1
                j += 1
            else:
                break
        return r
