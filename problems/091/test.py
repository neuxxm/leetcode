#18:24-18:39
def f(s, l, map):
    if l in map:
        return map[l]
    n = len(s)
    if n == 0:
        return 1
    if n == 1:
        if s[0] == '0':
            return 0
        return 1
    x = int(s[0])
    if x == 0:
        return 0
    if x >= 3:
        z = f(s[1:], l+1, map)
        map[l] = z
        return z
    elif x == 1:
        x2 = int(s[1])
        if x2 == 0:
            z = f(s[2:], l+2, map)
            map[l] = z
            return z
        else:
            z = f(s[1:], l+1, map) + f(s[2:], l+2, map)
            map[l] = z
            return z
    else:
        x2 = int(s[1])
        if x2 == 0:
            z = f(s[2:], l+2, map)
            map[l] = z
            return z
        elif x2 > 6:
            z = f(s[1:], l+1, map)
            map[l] = z
            return z
        else:
            z = f(s[1:], l+1, map) + f(s[2:], l+2, map)
            map[l] = z
            return z
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        map = {}
        return f(s, 0, map)
