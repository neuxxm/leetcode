#15:36-15:37
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        map = {}
        for x in paths:
            map[x[0]] = x[1]
        x = paths[0][0]
        while x in map:
            x = map[x]
        return x
