class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        h={}
        dummy=[]
        for i in words[0]:
            dummy.append(i)
        dummy2=[]
        dummy3=[]
        for i in range(1,len(words)):
            for j in range(0,len(words[i])):
                dummy2.append(words[i][j])
            for k in range(0,len(dummy)):
                if dummy[k] in dummy2:
                    dummy3.append(dummy[k])
                    dummy2.remove(dummy[k])
            
            dummy=dummy3
            dummy2=[]
            dummy3=[]
        print(dummy)
        
s=Solution()
s.commonChars(words = ["cool"])