class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            st = []
            # Split the string into parts of length k
            for i in range(0, len(s), k):
                st.append(s[i:i + k])
                
            str1 = ""
            # Compute the sum of digits for each part
            for part in st:
                val = sum(int(digit) for digit in part)
                str1 += str(val)
                
            s = str1
        
        print(s)
        

s = Solution()
s.digitSum(s = "11111222223", k = 3)  # Output: "27"
