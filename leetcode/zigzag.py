class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)==0:
            return 0
        if len(s)==1:
            return s
        le=len(s)
        row=0
        arr=["" for _ in range(numRows+1)]
        for i in range(le):
            arr[row]+=s[i]
            if row==0:
                down=True
            elif row==numRows-1:
                down=False 
            if down:
                row+=1
            else:
                row-=1
        
        return "".join(arr)
        

s=Solution()
print(s.convert(s = "PAYPALISHIRING", numRows = 3))