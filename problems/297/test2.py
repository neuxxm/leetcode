#21:11
class Codec:
    def serialize(self, root):
        if root == None:
            return 'None'
        q = [root]
        r = []
        while q:
            xs = []
            while q:
                x = q.pop(0)
                if x:
                    xs.append(x)
                    r.append(x.val)
                else:
                    r.append('None')
            for x in xs:
                q.append(x.left)
                q.append(x.right)

        return ','.join(rs)
    def f(a, i, n):
        if a[i] == 'None':
            return None
        l = i*2+1
        r = i*2+2
        x = TreeNode(int(a[i]))
        if l < n:
            x.left = f(a, l, n)
        if r < n:
            x.right = f(a, r, n)
        return x
    def deserialize(self, data):
        a = data.split(',')
        n = len(a)
        return f(a, 0, n)
