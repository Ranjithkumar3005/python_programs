class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If n is 0, return 0 (edge case)
        if n == 0:
            return 0
        
        # Start the stack with the first number
        st = [n]
        n -= 1
        c = 1

        while n > 0:
            if c == 1:
                st[-1] *= n  # Multiply
            elif c == 2:
                st[-1] //= n  # Integer divide
            elif c == 3:
                st.append(n)  # Addition
            else:
                st.append(-n)  # Subtraction
                c = 0
            n -= 1
            c += 1
        
        return sum(st)

s = Solution()
print(s.clumsy(10))  # Output should be 12
