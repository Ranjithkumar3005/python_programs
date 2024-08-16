class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if (start > destination):
            temp = start
            start = destination
            destination = temp
        
        val=0
        for i in range(start,destination):
            val+=distance[i]
        return min(val,(sum(distance)-val))

s=Solution()
print(s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))