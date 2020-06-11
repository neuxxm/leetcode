#23:46fail
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        a = T
        n = len(a)
        r = [0] * n
        q = []
        # 0  1  2  3  4  5
        # 73 74 75 71 69 72
        # [0] [] [1]
        # [] [2]
        # [2, 3, 4]
        # a[4] 
        for i in xrange(n):
            l = len(q)
            if l > 0:
                while l > 0:
                    if a[i] > a[q[l-1]]:
                        t = q.pop()
                        r[t] = i - t
                    else:
                        break
                    l = len(q)
                q.append(i)
            else:
                q.append(i)
        return r
