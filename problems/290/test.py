#20:21-20:35
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        start = 0
        end = 0
        cnt = 0
        s = str
        n = len(s)
        p = pattern
        m = len(p)
        map = {}
        map2 = {}
        for i in xrange(n):
            c = s[i]
            if c == ' ':
                if cnt < m:
                    w = s[start:i]
                    if w in map:
                        if map[w] != p[cnt]:
                            return False
                    else:
                        if p[cnt] in map2:
                            return False
                        map[w] = p[cnt]
                        map2[p[cnt]] = 1
                else:
                    return False
                start = i+1
                cnt += 1
        if cnt < m:
            w = s[start:]
            if w in map:
                if map[w] != p[cnt]:
                    return False
            else:
                if p[cnt] in map2:
                    return False
            cnt += 1
        else:
            return False
        return cnt == m
