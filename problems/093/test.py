#12:14-12:29
def f(s, k, t, z):
    if s == '':
        if k == 4:
            z.append(t[1:])
        return
    if k > 4:
        return
    n = len(s)
    if n == 1:
        f('', k+1, t + '.' + s, z)
        return
    m = int(s[0])
    if m > 2:
        f(s[1:], k+1, t + '.' + s[0], z)
        f(s[2:], k+1, t + '.' + s[:2], z)
    elif m == 0:
        f(s[1:], k+1, t + '.' + s[0], z)
    elif m == 1:
        f(s[1:], k+1, t + '.' + s[0], z)
        f(s[2:], k+1, t + '.' + s[:2], z)
        if n >= 3:
            f(s[3:], k+1, t + '.' + s[:3], z)
    else:
        if int(s[1]) > 5:
            f(s[1:], k+1, t + '.' + s[0], z)
            f(s[2:], k+1, t + '.' + s[:2], z)
        elif int(s[1]) < 5:
            f(s[1:], k+1, t + '.' + s[0], z)
            f(s[2:], k+1, t + '.' + s[:2], z)
            if n >= 3:
                f(s[3:], k+1, t + '.' + s[:3], z)
        else:
            f(s[1:], k+1, t + '.' + s[0], z)
            f(s[2:], k+1, t + '.' + s[:2], z)
            if n >= 3:
                if int(s[2]) <= 5:
                    f(s[3:], k+1, t + '.' + s[:3], z)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        z = []
        f(s, 0, '', z)
        return z
