class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        dummy=[]
        strs="ddd"
        count=1
        dummy1=[]
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
              if count>=3:
                dummy1.append(i-count+1)
                dummy1.append(i)
                dummy.append(dummy1)
                dummy1=[]
                count=1
              else:
                count=1
        
        print(dummy)
s=Solution()
s.largeGroupPositions(s = "aaa")