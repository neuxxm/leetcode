#14:57-15:30
def fa(s):
    n = len(s)
    map = {}
    for i in xrange(n):
        if s[i] != '9':
            map[s[i]] = '9'
            break
    buf = ''
    for i in xrange(n):
        c = s[i]
        if c in map:
            buf += map[c]
        else:
            buf += c
    return buf
def fb(s):
    n = len(s)
    map = {}
    last = s[0]
    b = True
    for i in xrange(n):
        if s[i] != last:
            b = False
            break
    if b:
        return '1' * n
    else:
        if s[0] == '1':
            i = 1
            buf = '1'
            map = {}
            while i < n:
                if s[i] != '1' and s[i] != '0':
                    map[s[i]] = '0'
                    break
                buf += s[i]
                i += 1
            for k in xrange(i, n):
                c = s[k]
                if c in map:
                    buf += map[c]
                else:
                    buf += c
            return buf
        else:
            buf = ''
            map[s[0]] = '1'
            for i in xrange(n):
                c = s[i]
                if c in map:
                    buf += map[c]
                else:
                    buf += c
            return buf
class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 9
        s = '%d'%num
        a = fa(s)
        b = fb(s)
        return int(a) - int(b)
