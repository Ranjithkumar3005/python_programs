class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination[:])
                return

            for i in range(start, n + 1):
                combination.append(i)
                print(combination)
                backtrack(i + 1, combination)
                combination.pop()

        result = []
        backtrack(1, [])
        return result   
        
        

s=Solution()
print(s.combine(n = 4, k = 2))