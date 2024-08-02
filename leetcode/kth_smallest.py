class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        coins=sorted(coins)
        ran=coins[0]*k
        dum=[]
        for i in range(0,len(coins)):
            sum=coins[i]
            j=1
            while j<=ran:
                dum.append(sum)
                sum+=coins[i]
                j+=1
            ran=dum[k-2]
    
        dum=sorted(list(set(dum)))
      
        print(dum[k-1])   
        
        

s=Solution()
s.findKthSmallest( coins = [3,6,9], k = 3)