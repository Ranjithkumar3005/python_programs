import math


class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        area = 0
        dia = 0
        for i in dimensions:
            length = float(math.sqrt(i[0] * i[0] + i[1] * i[1]))
            if length > dia:
                area = i[0] * i[1]
                dia = length
            elif length == dia:
                val = i[0] * i[1]
                if val > area:
                    area = val
        print(area)


s = Solution()
s.areaOfMaxDiagonal(dimensions=[[9, 3], [8, 6]])
