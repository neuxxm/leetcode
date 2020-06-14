#23:43-23:50
def f(s, i, n, map, z):
    if i == n:
        z.append(''.join(s))
        return
    if s[i] in map:
        c = s[i]
        list = [c, map[c]]
        for l in list:
            s[i] = l
            f(s, i+1, n, map, z)
            s[i] = c
    else:
        f(s, i+1, n, map, z)
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = []
        for c in S:
            s.append(c)
        n = len(s)
        str = 'abcdefghijklmnopqrstuvwxyz'
        map = {}
        for c in str:
            t = chr(ord(c)-ord('a')+ord('A'))
            map[c] = t
            map[t] = c
        z = []
        f(s, 0, n, map, z)
        return z
