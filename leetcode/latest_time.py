class Solution(object):
    def findLatestTime(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = list(s)
        for i in range(5):
            if arr[0] == '?':
                if arr[1] > '1' and arr[1] != '?':
                    arr[0] = '0'
                else:
                    arr[0] = '1'
            if arr[1] == '?':
                if arr[0] == '1':
                    arr[1] = '1'
                elif arr[0] == '0':
                    arr[1] = '9'
            if arr[3] == '?':
                arr[3] = '5'
            if arr[4] == '?':
                arr[4] = '9'
        return ''.join(arr)
             

s=Solution()
s.findLatestTime( s = "1?:?4")