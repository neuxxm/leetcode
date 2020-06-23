#21:53fail
def f(s):
    if s.isdigit():
        return [int(s)]
    i = 0
    n = len(s)
    res = []
    while i < n:
        c = s[i]
        if s[i] in set(['+', '-', '*']):
            left = f(s[:i])
            right = f(s[i+1:])
            for l in left:
                for r in right:
                    if c == '+':
                        res.append(l + r)
                    elif c == '-':
                        res.append(l - r)
                    elif c == '*':
                        res.append(l * r)
        i += 1
    return res
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        s = input
        return f(s)
