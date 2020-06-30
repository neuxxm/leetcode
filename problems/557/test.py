#13:53-13:56
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = []
        r = ''
        for c in s:
            if c != ' ':
                q.append(c)
            else:
                if len(q) > 0:
                    r += ''.join(q[::-1]) + ' '
                q = []
        if len(q) > 0:
            r += ''.join(q[::-1])
        return r
