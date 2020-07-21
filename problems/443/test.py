#15:44-15:57
def f(cnt, s, ix):
    r = []
    while cnt > 0:
        t = cnt%10
        r.append(t)
        cnt /= 10
    for d in r[::-1]:
        s[ix] = '%d'%d
        ix += 1
    return ix
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = chars
        n = len(s)
        last = s[0]
        ix = 0
        cnt = 1
        for i in xrange(1, n):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                if cnt == 1:
                    s[ix] = last
                    ix += 1
                else:
                    s[ix] = last
                    ix += 1
                    ix = f(cnt, s, ix)
                last = s[i]
                cnt = 1
        if cnt == 1:
            s[ix] = last
            ix += 1
        else:
            s[ix] = last
            ix += 1
            ix = f(cnt, s, ix)
        return ix
