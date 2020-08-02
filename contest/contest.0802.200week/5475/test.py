class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        n = len(arr)
        z = 0
        for i in xrange(n):
            for j in xrange(i+1, n):
                if abs(arr[i]-arr[j]) > a:
                    continue
                for k in xrange(j+1, n):
                    if abs(arr[j]-arr[k]) > b:
                        continue
                    if abs(arr[i]-arr[k]) <= c:
                        z += 1
        return  z
