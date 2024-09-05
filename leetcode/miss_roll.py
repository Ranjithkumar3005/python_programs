class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total_sum = mean * (n + m)
        observed_sum = sum(rolls)
        missing_sum = total_sum - observed_sum

        if missing_sum < n or missing_sum > 6 * n:
            return []

        result = [1] * n
        missing_sum -= n 
        
        for i in range(n):
            add = min(5, missing_sum)
            result[i] += add
            missing_sum -= add

        return result
        

s=Solution()
print(s.missingRolls(rolls = [1,5,6], mean = 3, n = 4))