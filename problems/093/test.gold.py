#13:15-13:24
def f(s, i, n, lvl, path, z):
    if lvl == 3:
        if i >= n:
            return
        if n-i>1 and s[i] == '0':
            return
        t = int(s[i:])
        if 0 <= t and t < 256:
            path[lvl] = s[i:]
            lvl += 1
            z.append('.'.join(path[:lvl]))
        return
    for j in xrange(1, 4):
        if i+j >= n:
            continue
        if j>1 and s[i] == '0':
            continue
        t = int(s[i:i+j])
        if 0 <= t and t < 256:
            path[lvl] = s[i:i+j]
            f(s, i+j, n, lvl+1, path, z)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        path = [''] * 4
        z = []
        f(s, 0, n, 0, path, z)
        return z
