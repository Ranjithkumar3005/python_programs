class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        st = []
        for i in range(len(prices)):
            while st and prices[st[-1]] >= prices[i]:
                idx = st.pop()
                prices[idx] -= prices[i]
            st.append(i)
        return prices

s = Solution()
print(s.finalPrices(prices = [8,4,6,2,3]))  # Output: [4,2,4,2,3]
