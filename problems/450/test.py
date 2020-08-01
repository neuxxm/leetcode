#21:01fail
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            x = root
            if x.left == None and x.right == None:
                return None
            if x.left == None:
                return x.right
            if x.right == None:
                return x.left
            p = x.right
            while p.left:
                p = p.left
            x.val = p.val
            #p = self.deleteNode(p, p.val)
            x.right = self.deleteNode(x.right, p.val)
            return x
