#15:16-16:38
def get(a, m):
    return a[m]
#%s/a.get(/get(a,/gc
#%s/get(a,/a.get(/gc
def update(ans, m):
    if ans == -1:
        ans = m
    else:
        if m < ans:
            ans = m
    return ans
def ispeak(a, m, n):
    t = a.get(m)
    return m>0 and m<n-1 and t>a.get(m-1) and t>a.get(m+1)
def search(a, l, r, y):
    ans = -1
    while l <= r:
        m = (l+r) >> 1
        t = a.get(m)
        if y == t:
            return m
        if y < t:
            r = m-1
        else:
            l = m+1
    return ans
def rsearch(a, l, r, y):
    ans = -1
    while l <= r:
        m = (l+r) >> 1
        t = a.get(m)
        if y == t:
            return m
        if y > t:
            r = m-1
        else:
            l = m+1
    return ans
class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        a = mountain_arr
        #n = len(a)
        n = a.length() 
        if n == 0:
            return -1
        y = target
        l = 0
        r = n - 1
        ans = -1
        peak = -1
        while l <= r:
            m = (l+r) >> 1
            if ispeak(a, m, n):
                if y == a.get(m):
                    return m
                peak = m
                break
            if m == 0:
                l += 1
                continue
            if m == n-1:
                r -= 1
                continue
            t = a.get(m)
            if t > a.get(m-1):
                l = m + 1
            else:
                r = m - 1
        if peak != -1:
            t = search(a, 0, peak-1, y)
            if t != -1:
                return t
            return rsearch(a, peak+1, n-1, y)
        else:
            return -1
