class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        c = 1
        indx = 1
        tot = 0
        h = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
        
        for i in range(1, len(word)):
            if h[word[i]] == h[word[i-1]]: 
                c += 1
            elif h[word[i]] > h[word[i-1]]:
                indx += 1
                c += 1
            else:  
                if word[i] == 'a':
                    indx = 1
                    c = 1
                else:
                    indx = 1
                    c = 0
            
            if indx == 5: 
                tot = max(tot, c)
                
        return tot


s=Solution()
s.longestBeautifulSubstring(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu")