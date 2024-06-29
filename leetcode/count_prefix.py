class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        c=0
        for i in words:
            if len(i)<=len(s) and i==s[0:len(i)]:
                print(i)
                c+=1
        print(c)
        
s=Solution()
s.countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc")