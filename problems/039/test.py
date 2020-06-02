#10:53-11:04
def f(i, j, zz, a, r):
    #print i, j, zz
    if j == 0:
        #print zz
        r.append(zz[:])
        return
    if i > 0:
        f(i-1, j, zz, a, r)
    if j >= a[i]:
        zz.append(a[i])
        f(i, j-a[i], zz, a, r)
        zz.pop()
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        a = candidates
        z = target
        n = len(a)
        zz = []
        r = []
        f(n-1, z, zz, a, r)
        return r
