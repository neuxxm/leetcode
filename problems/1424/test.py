#17:54-18:48
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        a = nums
        if len(a) == 0:
            return []
        n = len(a)
        q = [(0,0)]
        r = []
        visit = {}
        while len(q) > 0:
            i,j = q.pop(0)
            if (i,j) in visit:
                continue
            r.append(a[i][j])
            visit[(i,j)] = 1
            if i+1 < n and j < len(a[i+1]):
                q.append((i+1, j))
            if j+1 < len(a[i]):
                q.append((i, j+1))
        return r
