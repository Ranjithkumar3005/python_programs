class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        if k == 0:
            return [0] * n
        
        dum = []
        for i in range(n):
            sum_val = 0
            if k > 0:
                for j in range(1, k + 1):
                    sum_val += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    sum_val += code[(i - j) % n]
            dum.append(sum_val)
        
        return dum

# Example usage:
s = Solution()
print(s.decrypt(code = [5,7,1,4], k = 3))  # Output: [12, 10, 16, 13]
