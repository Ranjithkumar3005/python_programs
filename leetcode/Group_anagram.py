class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h={}
        c=0
        dumy=[]
        for i in range(0,len(strs)):
            dum="".join(sorted(strs[i]))
            if dum not in h:
                d=[]
                d.append(strs[i])
                dumy.append(d)
                h[dum]=c
                c+=1
            else:
                dumy[h[dum]].append(strs[i])
        print(dumy)
             
s=Solution()
s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])