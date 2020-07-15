#21:58-22:21
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ts = tokens
        q = []
        for t in ts:
            if t == '+':
                t2 = q.pop()
                t1 = q.pop()
                q.append(t1+t2)
            elif t == '-':
                t2 = q.pop()
                t1 = q.pop()
                q.append(t1-t2)
            elif t == '*':
                t2 = q.pop()
                t1 = q.pop()
                q.append(t1*t2)
            elif t == '/':
                t2 = q.pop()
                t1 = q.pop()
                r = t1/t2
                if t1 < 0 and t2 > 0:
                    r = -((-t1)/t2)
                elif t1 > 0 and t2 < 0:
                    r = -(t1/(-t2))
                q.append(r)
            else:
                q.append(int(t))
        return q.pop()
