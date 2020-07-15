#15:07
def f(s):
    n = len(s)
    b = True
    z = []
    for i in xrange(n):
        c = s[i]
        if c == '+' or c == '-' or c == '*':
            b = False
            t1 = f(s[:i])
            t2 = f(s[i+1:])
            if c == '+':
                for x in t1:
                    for y in t2:
                        z.append(x+y)
            elif c == '-':
                for x in t1:
                    for y in t2:
                        z.append(x-y)
            elif c == '*':
                for x in t1:
                    for y in t2:
                        z.append(x*y)
    if b:
        return [int(s)]
    else:
        return z
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        s = input
        return f(s)
a = "2*3-4*5"
#a = "2-1-1"
s = Solution()
print s.diffWaysToCompute(a)
