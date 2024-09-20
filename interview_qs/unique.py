class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dum=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        vals=set()
        for i in words:
            str1=""
            for j in i:
                str1+=dum[ord(j)-ord('a')]
            vals.add(str1)
        print(len(vals))   
        

s=Solution()
s.uniqueMorseRepresentations(words = ["gin","zen","gig","msg"])