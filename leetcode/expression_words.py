class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        c=0
        for i in range(0,len(words)):
            if len(words[i])>len(s):
                continue
            h1={}
            check=False
            for j in words[i]:
                if j not in h:
                    check=True
                    break
                if j in h1:
                    h1[j]+=1
                else:
                    h1[j]=1
            if len(h)!=len(h1) or check:
                continue
            for k in h1:
                if h1[k]>h[k]:
                    check=True
                    break
                if h[k]>h1[k]:
                    if h[k]<3:
                        check=True
                        break
            if check:
                continue
            c+=1
        print(c) 

s=Solution()
s.expressiveWords(s = "abcd", words = ["abcd"])        

