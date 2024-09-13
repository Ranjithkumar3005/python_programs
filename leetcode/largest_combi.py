class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        h={}
        
        for i in range(0,len(senders)):
            val=len(messages[i].split(" "))
            if senders[i] in h:
                h[senders[i]]+=val
            else:
                h[senders[i]]=val
        max1=max(h.values())
        dum=[]
        print(h)
        for i in h:
            if h[i]==max1:
                dum.append(i)
        dum=sorted(dum)
        return dum[len(dum)-1]
        

s=Solution()
print(s.largestWordCount(messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]))