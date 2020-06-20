# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#22:24
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = []
        q.append(root)
		r = ''
        while True:
            list = []
            while len(q) > 0:
                t = q.pop(0)
                list.append(t)
				r += '%d|'%(t.val)
            b = True
            for l in list:
                if l != None:
                    b = False
            if b:
                break
			for l in list:
				q.append(l.left)
				q.append(l.right)
		return r

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
