class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        strs=""
        for i in word:
            if i.isdigit():
                strs+=i
            else:
                strs+=" "
        dummy=strs.split(" ")
        s=[]
        for i in dummy:
            if i!="" and int(i) not in s:
                s.append(int(i))
        print(len(s))
        
s=Solution()
s.numDifferentIntegers(word = "a123bc34d8ef34")