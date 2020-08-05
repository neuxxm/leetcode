#13:37fail
def f(a, i, y, map):
    if (i,y) in map:
        return map[(i,y)]
    #print i, y
    if i == -1:
        if y == 0:
            return 1
        else:
            return 0
    t = sum(a[:i+1])
    if t < y:
        return 0
    t = f(a, i-1, y-a[i], map)
    t2 = f(a, i-1, y+a[i], map)
    map[(i,y)] = t + t2
    return t + t2
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        a = nums
        y = S
        n = len(a)
        map = {}
        return f(a, n-1, y, map)
