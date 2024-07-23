class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        output=[]
        def backtrack(current, index):
            if index == len(digits):
                output.append(current)
                return
            letters = keyboard[digits[index]]
            for letter in letters:
                backtrack(current + letter, index + 1)
        
        backtrack("", 0)
        return output
        
        

s=Solution()
s.letterCombinations(digits = "23")