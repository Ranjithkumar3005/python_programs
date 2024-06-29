class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        h={}
        for i in sentence:
            if i not in h:
                h[i]=1
        if len(h)==26:
            return True
        return False
        
s=Solution()
print(s.checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))