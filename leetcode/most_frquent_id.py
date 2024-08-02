class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        max1=0
        dum=[]
        dum1=[]
        
        for i in range(0,len(freq)):
            max1=max(max1,freq[i])
            if freq[i]<0:
                dum1.remove(abs(freq[i]))
                if dum1==[]:
                    max1=0
                else:
                 max1=max(dum1)
            if freq[i]>0:
              dum1.append(freq[i])
            dum.append(max1)
        print(dum)      
        

s=Solution()
s.mostFrequentIDs(  nums = [5], freq = [10])