class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def backtrack(index, curr):
            if index == len(arr):
                return len(curr)
            
            max_len = backtrack(index+1, curr)
            s = curr + arr[index]
            if len(s) == len(set(s)):  # unique
                max_len = max(max_len, backtrack(index+1, s))
            return max_len
        return backtrack(0, '')

        
        

s=Solution()
print(s.maxLength( arr = ["un","iq","ue"]))