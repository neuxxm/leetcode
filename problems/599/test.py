#16:38-16:43
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        map2 = {}
        for i,s in enumerate(list1):
            map2[s] = i
        map = {}
        for i,s in enumerate(list2):
            if s in map2:
                map[s] = map2[s] + i
        mi = float('inf')
        mik = ''
        for k,v in map.items():
            if v < mi:
                mi = v
                mik = k
        rs = []
        for k,v in map.items():
            if v == mi:
                rs.append(k)
        return rs
