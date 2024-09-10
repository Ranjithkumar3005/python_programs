class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        water = capacity

        for i, plant in enumerate(plants):
            steps += 1 
            if plant > water:
                steps += i 
                water = capacity  
                steps += i 
            water -= plant
        return steps     
        

s=Solution()
s.wateringPlants( plants =[3,2,4,2,1], capacity = 6)