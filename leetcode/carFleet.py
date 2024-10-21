class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        h = {}
        for i in range(0, len(position)):
            val = (target - position[i]) // speed[i]

            h[val] = 1
        print(len(h))


s = Solution()
s.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
