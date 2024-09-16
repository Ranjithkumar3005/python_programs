class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        part=[]
        
        def dfs(i):
            print(part)
            if i>=len(s):
                res.append(part[:])
                return 
            
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    print(s[i:j+1])
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res
    def isPali(self,s,l,r):
        if s[l:r+1]!=s[l:r+1][::-1]:
            return False
        return True        
        

s=Solution()
print(s.partition( s = "aab"))