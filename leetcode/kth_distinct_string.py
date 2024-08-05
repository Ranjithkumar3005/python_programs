class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        h={}
        dum=[]
        
        for i in arr:
            if i in h:
                h[i]+=1
                if i in dum:
                 dum.remove(i)
                 h[i]-=1
            else:
                h[i]=1
                dum.append(i)
        if len(dum)<k-1:
            return ""
        return dum[k-1]
        
        

s=Solution()
print(s.kthDistinct(["a","a"],k=1))