#0:10-0:11
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = S
        n = len(s)
        last = ''
        cnt = 0
        buf = ''
        for c in s:
            if c != last:
                if last != '':
                    buf += '%s%d'%(last, cnt)
                last = c
                cnt = 1                    
            else:
                cnt += 1
        if last != '':
            buf += '%s%d'%(last, cnt)
        if len(buf) < n:
            return buf
        else:
            return s
