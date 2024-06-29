class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        string = ["\0"] * 50
        i = 0
        while columnNumber > 0:
            rem = int(columnNumber % 26)
            if rem == 0:
                string[i] = 'Z'
                i += 1
                columnNumber = (columnNumber / 26) - 1
            else:
                string[i] = chr((rem - 1) + ord('A'))
                i += 1
                columnNumber = columnNumber / 26
        string[i] = '\0'
        string = string[::-1]
        print("".join(string))
        
s=Solution()
s.convertToTitle(25)