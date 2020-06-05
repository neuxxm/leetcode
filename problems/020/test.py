#14:54-14:56
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = []
        for c in s:
            l = len(q)
            if l > 0:
                if c == ')':
                    if q[l-1] == '(':
                        q.pop()
                    else:
                        q.append(c)
                elif c == ']':
                    if q[l-1] == '[':
                        q.pop()
                    else:
                        q.append(c)
                elif c == '}':
                    if q[l-1] == '{':
                        q.pop()
                    else:
                        q.append(c)
                else:
                    q.append(c)
            else:
                q.append(c)
        return len(q) == 0
