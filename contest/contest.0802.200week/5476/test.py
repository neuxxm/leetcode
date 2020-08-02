class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        a = arr
        n = len(a)
        ma = float('-inf')
        mak = 0
        if k < n:
            win = -1
            cnt = 0
            for i in xrange(1, n):
                if win == -1:
                    if a[i] > a[i-1]:
                        win = i
                        cnt = 1
                    else:
                        win = i-1
                        cnt = 1
                elif a[i] > a[win]:
                    win = i
                    cnt = 1
                else:
                    cnt += 1
                if cnt >= k:
                    break
            mak = win
        else:
            for i in xrange(n):
                if a[i] > ma:
                    ma = a[i]
                    mak = i
        return a[mak]
