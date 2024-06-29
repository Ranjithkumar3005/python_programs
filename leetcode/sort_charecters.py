class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        h={}
        for i in s:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        sorted_d = sorted(h.items(), key=lambda x: x[1], reverse=True)
        strs=""
        for i in sorted_d:
            strs+=i[0]*i[1]
        print(strs)
s=Solution()
s.frequencySort(s = "tree")