#7.8 15:46-16:32fail
def update(i, j, l, r, z):
    t = (j-i) * min(a[l], a[r])
    if t > z[0]:
        z[0] = t
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = height
        n = len(a)
        i = 0
        j = n-1
        z = 0
        while i < j:
            if a[i] < a[j]:
                t = (j-i) * a[i]
                if t > z:
                    z = t
                i += 1
            else:
                t = (j-i) * a[j]
                if t > z:
                    z = t
                j -= 1
        return z
