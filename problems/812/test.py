#21:31-21:39
import math
def g(x):
    return x*x
def dis(a, i, j):
    x = a[i][0]
    y = a[i][1]
    x2 = a[j][0]
    y2 = a[j][1]
    return math.sqrt(g(x-x2)+g(y-y2))
def f(arr, i, j, k):
    a = dis(arr, i, j)
    b = dis(arr, j, k)
    c = dis(arr, i, k)
    if a+b>c and b+c>a and a+c>b:
        p = (a+b+c) / 2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        return 0
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # sqrt(p*(p-a)*(p-b)*(p-c))
        a = points
        n = len(a)
        r = 0
        for i in xrange(0, n):
            for j in xrange(i+1, n):
                for k in xrange(j+1, n):
                    t = f(a, i, j, k)
                    if t > r:
                        r = t
        return r
