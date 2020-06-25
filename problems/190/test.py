#13:18-13:23
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        z = 0
        l = 31
        while n != 0:
            z |= ((n&1) << l)
            n >>= 1
            l -= 1
        return z
