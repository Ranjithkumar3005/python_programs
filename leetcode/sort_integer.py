class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        h={}
        
        for i in arr:
            val=str(bin(i))[2:]
            c=0
            for j in val:
                if j=="1":
                    c+=1
            if c in h:
                h[c].append(i)
            else:
                h[c]=[i]
        vals=sorted(h.items())
        dum=[]
        for i in vals:
            dum+=sorted(i[1])
        print(dum)
        
        

s=Solution()
s.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1])