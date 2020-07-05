#18:11-18:42
def f(x):
    if x >= 1000000000:
        r = f(x/1000000000) + ' Billion'
        z = x%1000000000
        if z != 0:
            r += ' ' + f(z)
        return r
    elif x >= 1000000:
        r = f(x/1000000) + ' Million'
        z = x%1000000
        if z != 0:
            r += ' ' + f(z)
        return r
    elif x >= 1000:
        r = f(x/1000) + ' Thousand'
        z = x%1000
        if z != 0:
            r += ' ' + f(z)
        return r
    elif x >= 100:
        r = f(x/100) + ' Hundred'
        z = x%100
        if z != 0:
            r += ' ' + f(z)
        return r
    else:
        dstr = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
                'Sixty', 'Seventy', 'Eighty', 'Ninety']
        t = x/10
        if t >= 2:
            r = dstr[t]
            z = x%10
            if z != 0:
                r += ' ' + f(z)
            return r
        elif t >= 1:
            dstr2 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
            return dstr2[x%10]
        else:
            dstr3 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 
                'Six', 'Seven', 'Eight', 'Nine']
            return dstr3[x]
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        return f(num)
