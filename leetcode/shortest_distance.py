class Solution(object):
    def closetTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        count=0
        count1=0
        if target not in words:
            return -1
        j=startIndex
        while True:
                if words[j]==target:
                    break
                count+=1
                j+=1
                if j==len(words):
                    j=0
        i=startIndex
        while True:
            if words[i]==target:
                break
            
            count1+=1
            i-=1
        print(count1," ",count)
        return min(count,count1)
s=Solution()
print(s.closetTarget(words =["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"],target ="zemkwvqrww",startIndex=8))