class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        strs="maa"
        dummy=""
        start=sentence[0]
        check=False
        for i in range(1,len(sentence)):
            if start in ['a','e','i','o','u','A','E','I','O','U']:
                dummy+=start
                start=""
            if sentence[i]==" ":
                dummy+=start+strs+" "
                strs+="a"
                if sentence[i+1] not in ['a','e','i','o','u']:
                   check=True
                else:
                    start=""
            elif check and sentence[i] not in ['a','e','i','o','u']:
                start=sentence[i]
                check=False
            else:
                dummy+=sentence[i]
        if " " not in sentence:
            if start in ['A','E','I','O','U']:
                dummy=sentence+strs
            else:
              dummy=dummy[0:len(dummy)]+start+strs
        else:
            dummy+=start+strs
        print(dummy)
        
s=Solution()
s.toGoatLatin(sentence = "Ass")