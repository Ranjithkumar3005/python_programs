class Solution:
    def sort_hm(self, s1,hm, keys):
        for k in keys:
            if hm[k] >0:
                s1 += k
                hm[k] -=1
        return s1, hm
    
    def sortString(self, s: str) -> str:
        # Logic is based on counts
        # Create hash map first
        hm = {}
        for i in s:
            hm[i] = hm.get(i,0) + 1
        
        s1=''
        while(len(s1) != len(s)):
            
            # step 1,2,3 of algoriths
            keys = sorted(hm)
            s1, hm = self.sort_hm(s1,hm, keys)

            # step 4,5,6 of algoriths
            keys = sorted(hm,reverse=True)
            s1, hm = self.sort_hm(s1,hm, keys)
            
        return s1
        
        
s=Solution()
print(s.sortString(s = "aaaabbbbcccc"))