class Solution():
    def dupli(self,arr):
        h={}
        for i in arr:
            if i in h:
                return i
            h[i]=1
        
        
        

s=Solution()
print(s.dupli(arr=[1,2,3,1,4]))