class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        st="22"
        max=0
        #st.is
        for i in range(0,len(strs)):
            if strs[i].isdigit():
                if max<int(strs[i]):
                    max=int(strs[i])
            else:
                if max<len(strs[i]):
                    max=len(strs[i])
        
        return max
s=Solution()
print(s.maximumValue( strs = ["3glko","1"]))