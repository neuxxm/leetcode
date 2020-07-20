#20:31-20:36
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = False
        seeNon = False
        r = 0
        for c in s:
            if c == ' ':
                if seeNon and not b:
                    r += 1
                b = True
            else:
                b = False
                seeNon = True
        if seeNon and not b:
            r += 1
        return r
