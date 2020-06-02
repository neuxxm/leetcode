#23:40-0:23
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        #0 1, 2, ..., n
        #1 n+1, n+2, ..., n+n
        #2 2n+1, 2n+2, ..., 2n+n
        #i=2 (0+1+2) * n
        # (0+i)*(i+1)*n
        tot = candies
        n = num_people
        r = [0] * n
        i = 0
        t = tot
        while True:
            z = (1+n)*n/2 + n*n*i
            if tot < z:
                break
            tot -= z
            i += 1
        z = n*i + 1
        k = 0
        while tot > 0:
            if tot >= z:
                r[k] += z
                tot -= z
            else:
                r[k] += tot
                break
            k += 1
            z += 1
        i -= 1
        for k in xrange(1, n+1):
            r[k-1] += (i+1)*k + i*(i+1)/2 * n
        return r
