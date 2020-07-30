#15:55-15:56
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        n = len(startTime)
        cnt = [0] * 1001
        for i in xrange(n):
            for j in xrange(startTime[i], endTime[i]+1):
                cnt[j] += 1
        return cnt[queryTime]
