class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = [-1]  # Initialize stack with -1 to handle base case
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    max_length = max(max_length, i - st[-1])
        
        return max_length

s = Solution()
print(s.longestValidParentheses("()(()"))  # Output should be 2
