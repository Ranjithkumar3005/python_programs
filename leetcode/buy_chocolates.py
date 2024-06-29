class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        total1=min(prices)
        prices.remove(total1)
        total2=min(prices)
        total=total1+total2
        return money-total if total<=money else money 
s=Solution()
print(s.buyChoco( prices = [1,2,3], money = 3))