class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        str=""
        check=True
        if ch in word:
            check=False
        for i in word:
            if check:
                str=str+i
            else:
                str=i+str
            if i==ch:
                check=True
            
        print(str)
        
s=Solution()
s.reversePrefix(word = "abcdefd", ch = "d")