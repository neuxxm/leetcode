# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#13:01-13:08
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
        x = root
        if x == None:
            return '#'
        l = self.serialize(x.left)
        r = self.serialize(x.right)
        return '%d'%(x.val) + ',' + l + ',' + r
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        a = data.rstrip(',').split(',')
        z = [0]
        return f(a, z)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
