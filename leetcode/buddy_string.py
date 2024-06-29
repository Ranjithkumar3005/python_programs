class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        h={}
        g={}
        if len(s)!=len(goal):
            return False
        else:
            for i in range(0,len(s)):
                if s[i] in h:
                    h[s[i]]+=1
                else:
                    h[s[i]]=1
                if goal[i] in g:
                    g[goal[i]]+=1
                else:
                    g[goal[i]]=1
        count=0
        if h!=g:
            return False
        else:
            for i in range(0,len(s)):
                if s[i]!=goal[i]:
                    count+=1
        dummy=list(h.values())
        if count==2 :
            return True
        elif count==0:
            for i in range(0,len(dummy)):
                if dummy[i]>=2:
                  return True
        return False
        
s=Solution()
print(s.buddyStrings(s = "aaab", goal = "aaab"))