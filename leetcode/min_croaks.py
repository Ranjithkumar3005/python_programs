class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        croak_count = [0] * 5
        max_frogs = 0
        current_frogs = 0
        croak_map = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        
        for char in croakOfFrogs:
            index=croak_map[char]
            croak_count[index] += 1
            if index > 0 and croak_count[index] > croak_count[index - 1]:
                return -1
            
            if char == 'c':
                current_frogs += 1
                max_frogs = max(max_frogs, current_frogs)
            elif char == 'k':
                current_frogs -= 1

        return max_frogs if croak_count[4] == croak_count[0] else -1
        
        

s=Solution()
print(s.minNumberOfFrogs(croakOfFrogs = "croakcrook"))