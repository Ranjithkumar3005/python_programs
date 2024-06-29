class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        h={}
        for i in arr:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        sorted_d = sorted(h.items(), key=lambda x: x[1])
        c=0
        for i in sorted_d:
            if k-i[1]<0:
                c+=1
            else:
                k=k-i[1]
        print(c)
s=Solution()
s.findLeastNumOfUniqueInts(arr = [2], k = 0)