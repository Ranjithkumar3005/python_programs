class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        h={}
        for i in hand:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        c=0
        ch=sorted(h.keys())
        while True:
           for i in range(0,groupSize):
               if i==groupSize-1:
                   h[ch[i]]-=1
                   print("ehllo")
                   break
               if h[ch[i]]==0:
                   #print(h)
                   ch.remove(ch[i])
                   print(ch," ",i)
               if ch[i]+1!=ch[i+1]:
                   print(ch)
                   return False
               else:
                   h[ch[i]]-=1    
                   print(h)
           if ch==[]:
                return True
        
        
s=Solution()
print(s.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))