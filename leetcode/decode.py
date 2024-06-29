class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        c=0
        h={}
        for i in range(0,len(key)):
            if key[i]==" ":
                continue
            elif key[i] not in h:
                h[key[i]]=chr(97+c)
                c+=1
        dummy=""
        for i in range(0,len(message)):
            if message[i]==" ":
                dummy+=message[i]
            else:
                dummy+=h[message[i]]
        
        print(dummy)
        
        
s=Solution()
s.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")