#23:35-23:36
def f(s):
    q = []
    for c in s:
        if c == '#':
            if len(q) > 0:
                q.pop()
        else:
            q.append(c)
    return ''.join(q)
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = f(S)
        t = f(T)
        return s == t
