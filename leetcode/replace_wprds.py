class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dum=sentence.split(" ")
        du=[]
        check=True
        c=0
        for i in dum:
            check=True
            for j in dictionary:
                if len(i)>len(j) and i[0:len(j)]==j and (c==0 or c>len(j)):
                    if c!=0:
                        du.pop()
                    c=len(j)
                    du.append(j)
                    check=False
            c=0
            if check:
                du.append(i)
                                       
        print(" ".join(du))     
s=Solution()
s.replaceWords(dictionary = ["catt", "cat", "aaa", "aaaa"], sentence = "cattle")