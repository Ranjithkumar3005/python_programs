class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        arr=text.split(" ")
        h={}
        for i in arr:
            val=len(i)
            if val in h:
                h[val].append(i)
            else:
                h[val]=[i]
                
        sorted_h=sorted(h.items())
        sorted_h[0][1][0]=sorted_h[0][1][0].capitalize()
        str2=sorted_h[0][1][0]
        for i in range(0,len(sorted_h)):
            for j in range(0,len(sorted_h[i][1])):
                if i==0 and j==0:
                    continue
                else:
                   str2+=" "+sorted_h[i][1][j].lower()
        print(str2)
        
        
        

s=Solution()
s.arrangeWords(text = "Keep calm and code on")