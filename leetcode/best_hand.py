class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        counter = {}
        for i in ranks:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        
        if len(set(suits)) == 1:
            return "Flush"
        elif max(counter.values()) >= 3:
            return "Three of a Kind"
        elif max(counter.values()) == 2:
            return "Pair"
        else:
            return "High Card"
        
        

s=Solution()
print(s.bestHand(ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]))