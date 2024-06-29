class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        h={}
        for i in arr:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        h2={}
        for i in h:
            if h[i] not in h2:
                h2[h[i]]=1
            else:
                return False
        return True
        

s=Solution()
print(s.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))