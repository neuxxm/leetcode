#12:25-12:32
class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        days = [''] * 32
        for i in xrange(1, 32):
            if i/10 == 1:
                tag = 'th'
            elif i%10 == 1:
                tag = 'st'
            elif i%10 == 2:
                tag = 'nd'
            elif i%10 == 3:
                tag = 'rd'
            else:
                tag = 'th'
            days[i] = '%d'%i+tag
        dmap = {}
        for i in xrange(1, 32):
            dmap[days[i]] = '%02d'%i
        months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        mmap = {}
        for i in xrange(1, 13):
            mmap[months[i]] = '%02d'%i
        ts = date.split(' ')
        d = dmap[ts[0]]
        m = mmap[ts[1]]
        y = ts[2]
        return y+'-'+m+'-'+d
