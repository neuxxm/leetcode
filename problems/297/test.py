# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#0:16fail
def f(a, z):
    i = z[0]
    if a[i] == '#':
        return None
    x = TreeNode(int(a[i]))
    z[0] += 1
    x.left = f(a, z)
    z[0] += 1
    x.right = f(a, z)
    return x
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 1,2,#,#,3,4,#,#,5,#,#
        if root == None:
            return '#,'
        l = self.serialize(root.left).rstrip(',')
        r = self.serialize(root.right).rstrip(',')
        return '%d'%(root.val) + ',' + l + ',' + r
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        a = data.split(',')
        n = len(a)
        z = [0]
        return f(a, z)
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
