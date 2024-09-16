class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        k = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res=[]
        def backtrack(n,curr):
            if len(curr)==len(digits):
                res.append(curr)
                return
            for i in k[digits[n]]:
                backtrack(n+1,curr+i)
        if digits: 
          backtrack(0,"")
        return (res)
        


s=Solution()
print(s.letterCombinations(digits = "23"))